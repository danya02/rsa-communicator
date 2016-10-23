#!/usr/bin/python3
import rsa
import json


def load_keybook():
    try:
        import os
        i = open(os.path.expanduser("~/.rsa-communicator/keybook.json"))
        obj = json.load(i)
        i.close()
        return obj
    except:
        raise EnvironmentError


def load_keys():
    try:
        import os
        i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "rb")
        pub = rsa.PublicKey.load_pkcs1(i.read())
        i.close()
        i = open(os.path.expanduser("~/.rsa-communicator/priv.key"), "rb")
        pri = rsa.PrivateKey.load_pkcs1(i.read())
        i.close()
        return (pub, pri)
    except:
        raise OSError


def encrypt(plaintext, key):
    return rsa.encrypt(plaintext, key)
if __name__ == '__main__':
    print("--- RSA encoder ---")
    print("Loading keys...", end=" ")
    try:
        keybook = load_keybook()
        pub, pri = load_keys()
    except EnvironmentError:
        print("FAILED.")
        print("Keybook not found or corrupted. Import some keys.")
        raise SystemExit(1)
    except OSError:
        print("FAILED.")
        print("Keypair not found or corrupted. Generate your keypair.")
    print("done.")
    print("Please select the index of the addressee...")
    for i in keybook:
        print(keybook.index(i)+1, ". ", i["name"])
    i = open(keybook[int(input("index: "))-1]["path"], "rb")
    key = rsa.PublicKey.load_pkcs1(i.read())
    i.close()
    print("Please enter the plaintext of the message on a single line...")
    plaintext = input()
    print("Encrypting message...", end=" ")
    encrypted_msg = encrypt(plaintext, key)
    print("done.")
    print("Your encrypted message is:")
    print()
    print(str(encrypted_msg)[2:-1])
