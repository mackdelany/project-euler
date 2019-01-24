# Euler problem 15
##########################
# Starting in the top left corner of a 20×20 grid, and only being able
# to move to the right and down, how many possibe routes are there
# to the bottom right corner?

import time
start = time.time()

import numpy as np

gridSize = 20
numMoves = gridSize*2

## there has to be at least 20 rights and 20 downs
## take right to be 1, down to be 0

base = np.zeros(numMoves)

routeEnd = 0
routeCount = 0
routes = np.zeros(0)

while routeEnd = 0:

    rightCount = 0
    downCount = 0

    routes = np.vstack((routes, base)

    for x in numMoves:
        movesMade = rightCount + downCount
        if rightCount < gridSize and routes[routeCount,0:movesmade] != :
            rightCount += 1
            routes((routeCount-1),x) = 1
        elif

    routeCount += 1

print(routes)
                       
print("This took " + str(time.time() - start) + " seconds")
