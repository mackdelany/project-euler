# Euler problem 25
##########################
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time
start = time.time()

fibs = [1,1]
index = [1,2]

while len(str(fibs[-1])) < 1000:
    fibs.append(fibs[-1]+fibs[-2])
    index.append(index[-1] + 1)

print("The answer is " + str(index[-1]))

print("It took " + str(time.time() - start) + " seconds")
