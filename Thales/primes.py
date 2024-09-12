import numpy as np
import random
import time
import matplotlib.pyplot as plt
from numba import njit
from numba.typed import Dict
from numba.core import types

@njit
def sieve_of_eratosthenes(n):
    primebits = np.ones(n + 1, dtype=np.bool_)
    primebits[0:2] = False
    for p in range(2, int(np.sqrt(n)) + 1):
        if primebits[p]:
            primebits[p*p::p] = False
    return np.flatnonzero(primebits)

@njit
def check_goldbach(n, primes, prime_set, cache):
    if n in cache:
        return cache[n]
    
    numpairs = 0
    N = n // 2
    
    if n == 4:
        cache[n] = 1
        return 1
    
    for p in primes:
        if p > N:
            break
        if (n - p) in prime_set:
            numpairs += 1
    
    cache[n] = numpairs
    return numpairs

@njit
def main_all(n):
    even_range = np.arange(4, n + 1, 2)
    primes = sieve_of_eratosthenes(n)
    
    prime_set = set(primes)
    cache = Dict.empty(key_type=types.int64, value_type=types.int64)
    
    # For all even numbers, calculate the Goldbach pairs
    checks = np.zeros(len(even_range), dtype=np.int64)
    for i in range(len(even_range)):
        checks[i] = check_goldbach(even_range[i], primes, prime_set, cache)
    
    return even_range, checks

if __name__ == "__main__":
    n = 10**6  # You can adjust the upper limit here

    start_time = time.time()
    even_range, checks = main_all(n)  # Call the updated function
    end_time = time.time()

    print(f"Total execution time: {end_time - start_time:.2f} seconds")

    if np.any(checks == 0):
        print("Found a counter example for Goldbach")

    # Plot all even numbers with their Goldbach pairs
    plt.scatter(even_range, checks, s=0.01)
    plt.xlabel('n')
    plt.ylabel('Number of Goldbach pairs')
    plt.show()
