#!/usr/bin/python3
import rsa
import argparse


def parse():
    parser = argparse.ArgumentParser(description='Generate a keypair.')
    parser.add_argument('complexity', metavar='complex', type=int,
                        help='complexity of keypair')
    parser.add_argument('name', metavar='name', type=str,
                        help='name of owner')
    parser.add_argument('--dry', action='store_true',
                        help='do not save results')
    parser.add_argument('-q', action='store_false',
                        help='do not display any output')
    parser.add_argument('-v', '--version', action='version',
                        version='1.0')
    return parser.parse_args()


def keys(com):
    import multiprocessing
    return rsa.newkeys(com, poolsize=multiprocessing.cpu_count())


def save(pub, pri, name):
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
    i = open(os.path.expanduser("~/.rsa-communicator/name"), "w")
    i.write(name)
    i.close()
if __name__ == '__main__':
    args = parse()
    if args.q:
        print("--- RSA keypair generator ---")
    comp = args.complexity
    if args.q:
        print("Generating keypair...", end=" ")
    pub, pri = keys(comp)
    if args.q:
        print("done.")
    name = args.name
    if not args.dry:
        if args.q:
            print("Saving keys...", end=" ")
        save(pub, pri, name)
        if args.q:
            print("done.")
