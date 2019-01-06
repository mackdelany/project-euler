# Euler problem 39
##########################
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p < 1000, is the number of solutions maximised?


##c=a2+b2
import numpy as np

numP = 1000
ans = np.zeros((numP,2))


for p in range(numP):
    count = 0
    ans[p,0] = p + 1

    #for x in p:
    for x in range(int(ans[p,0])):
        c = x + 1
        c2 = c**2
        for y in range(c):
            a = y + 1
            if c2 == ((a**2) + ((int(ans[p,0])-c-a)**2)):
                ans[p,1] += 1
                if ans[p,1] == 28:
                    print(p)


ans1 = np.argmax(np.max(x, axis=1))

print(ans1)
