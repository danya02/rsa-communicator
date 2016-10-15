#!/usr/bin/python3
import rsa


def keys(com):
    import multiprocessing
    return rsa.newkeys(com, poolsize=multiprocessing.cpu_count())


def save(pub, pri):
    import os
    try:
        os.makedirs(os.path.expanduser("~/.rsa-communicator"))
    except:
        pass
    i = open(os.path.expanduser("~/.rsa-communicator/priv.key"), "wb")
    i.write(pri.save_pkcs1())
    i.close()
    i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "wb")
    i.write(pub.save_pkcs1())
    i.close()
if __name__ == '__main__':
    print("--- RSA keypair generator ---")
    comp = int(input("complexity of key: "))
    print("Generating keypair...", end=" ")
    pub, pri = keys(comp)
    print("done.")
    print("Saving keys...", end=" ")
    save(pub, pri)
    print("done.")
