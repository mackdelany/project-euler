# Euler problem 48
##########################
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time

start = time.time()
Sum = 0

for number in range(1,1001):
    Sum += (number ** number)

finalSum = str(Sum)
lengthMinusTen = len(finalSum) - 10
digit10 = finalSum[lengthMinusTen:]

print(Sum)
print("The answer is: " + str(digit10))
print("This took " + str(time.time() - start) + " seconds")
