filepath = 'input.txt'

walls = {}
maxindex = 0

with open(filepath) as fp:
    for line in fp:
      (index,depth) = line.split(": ")
      if int(index) > maxindex:
          maxindex = int(index)
      walls[int(index)]=(int(depth),0,1) #depth, location, direction

print("maxindex {}".format(maxindex))


def updateWalls(walls):
    for index, (depth,atIndex,direction) in walls.items():
        #we are at the end of the array
        if depth != 0 and depth-1 == atIndex and direction == 1:
            direction = -1 * direction
        #we are at the beginning of the array
        if depth != 0 and atIndex == 0 and direction == -1:
            direction = -1 * direction

        walls[index] = (depth,atIndex + 1 * direction, direction)

    return walls

currentwalls = dict(walls)
delay = 1


while True:
    totalCost = 0
    currentwalls = updateWalls(currentwalls)
    workingwalls = dict(currentwalls)

    for e in range(maxindex+1):
       wallAtE = workingwalls.get(e,(0,0,0))
       if wallAtE != (0,0,0):
           if wallAtE[1] == 0 :
               totalCost = totalCost + (e*wallAtE[0])
               #print("totalCost1 {}".format(totalCost))
               if totalCost > 0 :
                   break
       workingwalls = updateWalls(workingwalls)
    else:
        if totalCost == 0:
             print("Found proper delay {}".format(delay))
             print(workingwalls)
             break;
    if delay % 10000 == 0:
        print(delay)

    delay = delay + 1
