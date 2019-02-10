# Euler problem 3
##########################
# What is the largest prime factor of the number 600851475143?

import time
start = time.time()

bigNumber = 600851475143

def largest_prime_factor(bigNumber):
    potentialFactor = 2
    while potentialFactor * potentialFactor <= bigNumber:
        if bigNumber % potentialFactor:
            potentialFactor += 1
        else:
            bigNumber //= potentialFactor
    return bigNumber

ans = largest_prime_factor(bigNumber)
print(ans)

print("This took " + str(time.time() - start) + " seconds")
