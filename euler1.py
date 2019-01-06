# Euler problem 1
##########################
# Multiples of 3 and 5

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

numbers = list(range(1,1000))

result = []

for items in numbers:
    if items % 3 == 0:
        result.append(items)
    elif items % 5 == 0:
        result.append(items)

multiple = sum(result)
print(multiple)
