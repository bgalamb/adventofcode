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


totalCost = 0
for e in range(maxindex+1):
   wallAtE = walls.get(e,(0,0,0))
   #print("wallAt {} = {}".format(e, wallAtE))
   if wallAtE != (0,0,0):
       if wallAtE[1] == 0 :
           totalCost = totalCost + (e*wallAtE[0])
           print("totalCost {}".format(totalCost))

   walls = updateWalls(walls)
