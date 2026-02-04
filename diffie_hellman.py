#!/usr/bin/env python

import secrets
import miller_rabin


def get_modulous_and_generator():
    while True:
        q = miller_rabin.generate_prime(1024)
        p = 2*q + 1
        print('q found!')
        if miller_rabin.miller_rabin(p):
            print('p found!')
            while True:
                g = secrets.randbelow(p-3) + 2

                if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
                    return p, g


def main():
    # Step 1: Alice and Bob agree on a modulous, n, and generator, g
    n, g = get_modulous_and_generator()

    # Step 2: Alice and Bob choose a private key, a and b respectively, where 1 < a,b < n -1
    a = secrets.randbelow(n - 3) + 2
    b = secrets.randbelow(n - 3) + 2

    # Step 3: Alice and Bob compute their public keys, A and B respectively
    A = pow(g, a, n)
    B = pow(g, b, n)

    # Step 4: Alice and Bob share their public keys publicly with each other
    # Step 5: Alice and Bob comppute the shared secret key, key
    k_alice = pow(B, a, n)
    k_bob = pow(A, b, n)

    # Check that these keys match
    if k_alice == k_bob:
        print('Keys Match!')
        print(f'Key: {k_alice}')
    else:
        print('Keys do not match')
        print(f'Alice\'s Key: {k_alice}')
        print(f'Bob\'s Key: {k_bob}')


if __name__ == '__main__':
    main()

