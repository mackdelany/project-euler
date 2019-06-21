# Euler problem 56
##########################
# A googol is a large number, 10^100, one followed by one hundred zeros
# 100^100 is also very large, one followed by two hundred zeros
# Despite their size, the sum of the digits in each number is only 1
# Considering natural numbers of the form, a^b, where a,b < 100, what is the maximum digital sum?

import time
start = time.time()

numbers = list(range(1,100))

digitalSumMax = 0

for a in numbers:
    for b in numbers:

        naturalNumber = a ** b

        naturalNumberString = str(naturalNumber)

        digitalSumCount = 0

        for digit in range(0,len(naturalNumberString)):

            digitalSumCount += int(naturalNumberString[digit])

        if digitalSumCount >= digitalSumMax:

            digitalSumMax = digitalSumCount 

print("The maximum digital sum is " + str(digitalSumMax))

print("This took " + str(time.time() - start) + " seconds")
