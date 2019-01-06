# Euler problem 65
##########################
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

# create n100 terms matrix

terms = [2]

for n in range(1 , 34):
    n = n * 2

    terms.append(1)
    terms.append(n)
    terms.append(1)

# find n100 for e
convergent = 99 ## number fraction, 9 to check, 99 for problem

conv = terms[convergent]
conv = float(conv)

for x in range(convergent-1, -1 , -1):
    i = float(terms[x])
    conv = (1 / conv)
    float(conv)
    conv = conv + i
    float(conv)


# change to  fraction
a = (conv).as_integer_ratio()

# remove numerator
num = a[0]

# sum digits
digits = map(int, str(num))
final = sum(digits)
print(final)
