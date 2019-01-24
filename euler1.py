# Euler problem 1
##########################
# Multiples of 3 and 5

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import time
start = time.time()

numbers = list(range(1,1000))
multiples = []

for items in numbers:
    if items % 3 == 0:
        multiples.append(items)
    elif items % 5 == 0:
        multiples.append(items)

sumOfMultiples = sum(multiples)
print(sumOfMultiples)

print("This took " + str(time.time() - start) + " seconds")
