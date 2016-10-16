#!/usr/bin/python3

import socket


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


def load_key():
    import os
    i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "rb")
    pub = i.read()
    i.close()
    i = open(os.path.expanduser("~/.rsa-communicator/name"))
    name = i.read()
    i.close()
    return (pub, name)
if __name__ == '__main__':
    print("--- RSA key sharer ---")
    role = input("Should I (R)eceive or (S)end key data? ").upper()
    while not role == "R" and not role == "S":
        print("Please enter R or S.")
        role = input("Should I (R)eceive or (S)end key data? ").upper()
    if role == "S":
        s = socket.socket()
        s1 = socket.socket()
        s1.connect(("8.8.8.8", 53))
        host = s1.getsockname()[0]
        s1.close()
        import random
        port = random.randint(1024, 65535)
        s.bind(("0.0.0.0", port))
        s.listen(0)
        key, name = load_key()
        import json
        message = json.dumps({"name": name, "key": str(key)[2:-1]})
        print("Listening for connections... (press ^C to stop)")
        print("Tell your partner to connect to host", host, "and port", port)
        while 1:
            c, addr = s.accept()
            c.setblocking(True)
            print("Connected, recieving authentication key...", end=" ")
            auth = bytes()
            for i in range(4):
                auth += c.recv(1)
            authkey = auth.hex().upper()
            print("done.")
            print("Recieved connection from address", addr,
                  "with authentication key", authkey+".")
            if input(
             "Does this mirror your observations? (y/N) ").upper() == "Y":
                print("Transmitting data...", end=" ")
                c.sendall(bytes(message, "utf-8"))
                c.close()
                print("done.")
    else:
        s = socket.socket()
        s1 = socket.socket()
        s1.connect(("8.8.8.8", 53))
        host = s1.getsockname()[0]
        s1.close()
        host = input("IP address/hostname: ")
        port = int(input("port: "))
        import os
        import json
        key = os.urandom(4)
        hexkey = key.hex().upper()
        s.connect((host, port))
        print("Your authorization key id:", hexkey)
        s.sendall(key)
        s.settimeout(30)
        message = s.recv(8192)
        if message == b"":
            print("Recieved null message, try again.")
            raise SystemExit(1)
        jsonobj = json.loads(str(message)[2:-1])
        print("Received keybook entry of ", jsonobj["name"], "", sep="'")
        if input(
         "Should it be added to the keybook? (y/N) ").upper() == "Y":
            print("Saving key...", end=" ")
            obj = {"name": jsonobj["name"]}
            os.makedirs(os.path.expanduser("~/.rsa-communicator/keys"))
            key = jsonobj["key"]
            import uuid
            keysave = open(os.path.expanduser(
                "~/.rsa-communicator/keys/"+uuid.uuid4()), "wb")
            keysave.write(key)
            keysave.close()
            obj["path"] = keysave.name
            add_object(obj)
