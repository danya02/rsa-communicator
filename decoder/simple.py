#!/usr/bin/python3
import rsa


def load_keys():
    import os
    i = open(os.path.expanduser("~/.rsa-communicator/pub.key"), "rb")
    pub = rsa.PublicKey.load_pkcs1(i.read())
    i.close()
    i = open(os.path.expanduser("~/.rsa-communicator/priv.key"), "rb")
    pri = rsa.PrivateKey.load_pkcs1(i.read())
    i.close()
    return (pub, pri)


def decrypt(msg, key):
    return rsa.decrypt(msg, key)
if __name__ == '__main__':
    print("--- RSA decoder ---")
    print("Loading keys...", end=" ")
    try:
        pub, pri = load_keys()
    except:
        print("FAILED.")
        print("Keypair not found or corrupted. Generate your keypair.")
        raise SystemExit(1)
    print("done.")
    print("Please enter the cyphertext of the message on a single line...")
    cyphertext = bytes(input(), "utf-8")
    print("Decrypting message...", end=" ")
    try:
        decrypted_msg = decrypt(cyphertext, pri)
    except:
        print("FAILED.")
        print("Unable to decrypt message, wrong keypair or message corrupted?")
    print("done.")
    print("Your decrypted message is:")
    print()
    print(decrypted_msg)
