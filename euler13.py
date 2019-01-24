# Euler problem 13
##########################
# Work out the first ten digits of the sum of the one-hundred 50-digit numbers
# in the file 'euler13_numbers.txt'

import time
start = time.time()

filename = 'euler13nums.txt'
with open(filename, "r") as nums:

    ## write numbers to array
    numbersStr = []

    for line in nums:
        numbersStr.append(line)

## convert array to int
numbersInt = []

for x in numbersStr:
    numbersInt.append(int(x))

print(sum(numbersInt))
