# Euler problem 21
##########################
# Evaluate the sum of all the amicable numbers under 10000.

import time, math
start = time.time()

amicable_nums = set()

def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

for i in range(1, 10000):
    sdi = sum_div(i)
    for j in range(i+1, 10000):
        if sdi == j and sum_div(j) == i:
            amicable_nums.update([i, j])

print(sum(amicable_nums))
print("This took " + str(time.time() - start) + " seconds")
