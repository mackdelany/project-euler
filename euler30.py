# Euler problem 30
##########################
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time

start = time.time()

def isFifthPower(n):
    num = str(n)
    sum = 0

    for x in range(len(num)):
        sum += int(num[x])**5

    if sum == n:
        return True
    else:
        return False


fifthNumbers = []

for i in range(1000000):
    if isFifthPower(i):
        fifthNumbers.append(i)


ans = sum(fifthNumbers) - 1
print("The answer is:" +  str(ans))
print("It took " + str(time.time() - start) + " seconds")
