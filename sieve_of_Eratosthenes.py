#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:30:50 2020

No wheel Sieve of Eratosthenes

@author: luke
"""

import gmpy2

def build_sieve(num):
    numroot = gmpy2.isqrt(num)
    size = num
    init = [True] * (size)
    for i in range(2, numroot):
        if init[i]:
            for j in range(i**2, num, i):
                init[j] = False
    primes = []
    for i in range(2, len(init)):
        if init[i]:
            primes.append(i)
    return primes


primes = build_sieve(10000)
print(primes)