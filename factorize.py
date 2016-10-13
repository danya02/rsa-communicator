#!/usr/bin/python3
from sympy.ntheory import factorint


def factor(num):
    return factorint(int(num))

if __name__ == '__main__':
    print("Answer:", factor(input("number to factor:")))
