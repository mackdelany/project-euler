"""
EULER PROBLEM 14: Collatz Problem

The following iterative sequence is defined for the set of positive integers.:

N -> N/2 (N is even)
N -> 3N + 1 (N is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40  -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that the sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proven yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number under one million, produces the longest chain?
"""

import time

start = time.time()

def isOdd(N):
    return ((N%2) != 0)

def sequenceForEven(N):
    return (N/2)

def sequenceForOdd(N):
    return ((3*N) + 1)

lengthOfLongestChain = 0
NOfLongestChain = 0


for N in range(2,1000001):
    startingN = N
    sequenceCount = 0

    while N > 1:
        if isOdd(N):
            N = sequenceForOdd(N)
        else:
            N = sequenceForEven(N)

        sequenceCount += 1

    if sequenceCount > lengthOfLongestChain:
        lengthOfLongestChain = sequenceCount
        startingNOfLongestChain = startingN

        
print('The longest chain was ' + str(lengthOfLongestChain) + ' numbers')
print('This chain came from the number: ' + str(startingNOfLongestChain))

print('This took: ' + str(time.time() - start) + ' seconds')

#837799