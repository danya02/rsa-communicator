#!/usr/bin/python3
import json


def add_object(diction):
    import os
    try:
        obj = json.load(open(
            os.path.expanduser("~/.rsa-communicator/keybook.json")))
    except:
        obj = []
    obj += [diction]
    json.dump(obj, open(
        os.path.expanduser("~/.rsa-communicator/keybook.json")))
if __name__ == '__main__':
    print("--- RSA keybook mantainer ---")
    print("Adding a keybook entry...")
    correct = False
    obj = {}
    while not correct:
        obj["name"] = input("Name: ")
        keypath = input("Path to key file: ")
        if input("Is this information correct? (y/N) ").capitalize() == "Y":
            correct = True
            import os
            os.makedirs(os.path.expanduser("~/.rsa-communicator/keys"))
            key = open(os.path.abspath(os.path.expanduser(keypath)), "rb").read()
            import uuid
            keysave = open(os.path.expanduser(
                "~/.rsa-communicator/keys/"+uuid.uuid4()), "wb")
            keysave.write(key.replace("\\n", "\n"))
            keysave.close()
            obj["path"] = keysave.name
    add_object(obj)
