#!/usr/bin/python3
import rsa
import paho.mqtt.client as mqtt


def load_keys():
    import os
    i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "rb")
    pub = rsa.PublicKey.load_pkcs1(i.read())
    i.close()
    i = open(os.path.expanduser("~/.rsa-communicator/priv.key"), "rb")
    pri = rsa.PrivateKey.load_pkcs1(i.read())
    i.close()
    return (pub, pri)


def decrypt(msg):
    global decrypt_key
    return rsa.decrypt(msg, decrypt_key)


def load_keybook():
    import os
    import json
    i = open(os.path.expanduser("~/.rsa-communicator/keybook.json"))
    obj = json.load(i)
    i.close()
    return obj


def encrypt(plaintext):
    global encrypt_key
    return rsa.encrypt(plaintext, encrypt_key)


def on_acquire(client, userdata, message):
    print(">", decrypt(message.payload))

if __name__ == '__main__':
    print("--- RSA chat ---")
    print("Please enter the IP address of your MQTT server and your",
          "chat room name...")
    keybook = load_keybook()
    keys = load_keys()
    global decrypt_key
    decrypt_key = keys[1]
    addr = input("IP address: ")
    topic = input("chat room: ")
    print("Please select the addressee's index:")
    for i in keybook:
        print(keybook.index(i)+1, ". ", i["name"], sep="")
    i = open(keybook[int(input("index: "))-1]["path"], "rb")
    global encrypt_key
    encrypt_key = rsa.PublicKey.load_pkcs1(i.read())
    i.close()
    m = mqtt.Client()
    m.connect(addr)
    m.subscribe((topic, 2))
    m.on_message = on_acquire
    m.loop_start()
    print("Enter messages below, press <ENTER> when they are to be sent.")
    try:
        while 1:
            message = input()
            print(" (Message being encrypted and sent...)",
                  end="\r", flush=True)
            message = encrypt(message)
            m.publish(topic, payload=message)
            print("\033[K", end="", flush=True)
    except KeyboardInterrupt:
        m.loop_stop()
        m.disconnect()
        print("=== DISCONNECTED ===")
    except EOFError:
        m.loop_stop()
        m.disconnect()
        print("=== DISCONNECTED ===")
