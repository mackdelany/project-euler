# Euler problem 3
##########################
# What is the largest prime factor of the number 600851475143?

import time
start = time.time()

bigPrime = 600851475143

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

ans = largest_prime_factor(bigPrime)
print(ans)
