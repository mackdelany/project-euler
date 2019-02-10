# Euler problem 13
##########################
# Work out the first ten digits of the sum of the one-hundred 50-digit numbers
# in the file 'euler13_numbers.txt'

import time
start = time.time()

filename = 'euler13nums.txt'

# Write numbers to array
with open(filename, "r") as numbers:
  
    numberArray = []

    for line in numbers:
        numberArray.append(line)

# Convert array to int
numberArrayInt = []

for x in numberArray:
    numberArrayInt.append(int(x))

print(sum(numberArrayInt))
print("This took " + str(time.time() - start) + " seconds")
