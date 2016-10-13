#!/usr/bin/python3
import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi



def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


if __name__ == '__main__':
    print("--- RSA keypair generator ---")
    if input("Do you want to enter primes yourself? (y/N) ").capitalize() == "Y":
        p, q = input("two primes, separated by a space: ").split(" ")
    else:
        import random
        import pyprimes
        p = pyprimes.primes()
        primes = [next(p) for _ in range(10000)]
        p = random.choice(primes)
        primes.remove(p)
        q = random.choice(primes)
        primes.remove(q)
        print("Your primes are:", p, "and", str(q)+".")
    print("Generating keypair...", end=" ")
    pub, pri = generate_keypair(p, q)
    print("done.")
    print("Your public key is ", public, "and your private key is ", private)
