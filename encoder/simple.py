#!/usr/bin/python3
import rsa
import json


def load_keybook():
    import os
    i = open(os.path.expanduser("~/.rsa-communicator/keybook.json"))
    obj = json.load(i)
    i.close()
    return obj


def load_keys():
    import os
    i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "b")
    pub = rsa.PublicKey.load_pkcs1(i.read())
    i.close()
    i = open(os.path.expanduser("~/.rsa-communicator/priv.key"), "b")
    pri = rsa.PrivateKey.load_pkcs1(i.read())
    i.close()
    return (pub, pri)


def encrypt(plaintext, key):
    return rsa.encrypt(plaintext, key)
if __name__ == '__main__':
    print("--- RSA encoder ---")
    print("Loading keys...", end=" ")
    keybook = load_keybook()
    pub, pri = load_keys()
    print("done.")
    print("Please select the index of the addressee...")
    for i in keybook:
        print(keybook.index(i)+1, ". ", i["name"])
    i = open(keybook[int(input("index: "))+1]["path"], "b")
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
