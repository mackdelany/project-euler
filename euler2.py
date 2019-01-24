# Euler problem 2
##########################
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

import time
start = time.time()

numbers = list(range(1,1000))
fib = [1 , 2]

from remove_odd import remove_odd

while fib[-1] < 4000000:
    input = fib[-1] + fib[-2]
    fib.append(input)

result = remove_odd(fib)

sum = sum(result)

print(sum)
