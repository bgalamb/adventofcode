#number, coordx, coordy
matrix = {(0,0):1}
coord = [0,0]
directions=["right","up","left","down"]

def cangotodirection(direction):
    #right
    if direction == "right":
        if (coord[0]+1,coord[1]) in matrix:
            return False
    #left
    if direction == "left":
        if (coord[0]-1,coord[1]) in matrix:
            return False
    #up
    if direction == "up":
        if (coord[0],coord[1]+1) in matrix:
            return False
    #down
    if direction == "down":
        if (coord[0],coord[1]-1) in matrix:
            return False

    return True

def gotodirection(direction):
    #right
    if direction == "right":
        matrix[(coord[0]+1,coord[1])] = getadjacentvals((coord[0]+1,coord[1]))
        coord[0] = coord[0]+1
    #left
    if direction == "left":
        matrix[(coord[0]-1,coord[1])] = getadjacentvals((coord[0]-1,coord[1]))
        coord[0] = coord[0]-1
    #up
    if direction == "up":
        matrix[(coord[0],coord[1]+1)] = getadjacentvals((coord[0],coord[1]+1))
        coord[1] = coord[1]+1
    #down
    if direction == "down":
        matrix[(coord[0],coord[1]-1)] = getadjacentvals((coord[0],coord[1]-1))
        coord[1] = coord[1]-1

    #print(matrix)

def getadjacentvals(coord):
    val = 0
    #print("****************")
    #print("coord in {}".format((coord[0],coord[1])))
    for xoffs in range(-1,2):
        for yoffs in range(-1,2):
            #print("xoffs, yoffs = {}, {}".format(xoffs,yoffs))
            if (coord[0]+xoffs,coord[1]+yoffs) in matrix:
                #print("value at ({},{}) = {}".format(coord[0]+xoffs,coord[1]+yoffs,matrix[coord[0]+xoffs,coord[1]+yoffs]))
                val += matrix[coord[0]+xoffs,coord[1]+yoffs]
    #print("sum of adjacent vals of {} is {}".format((coord[0],coord[1]),val))
    return val


directionindx = 0
elem = 1
while True:
    direction = directions[directionindx % len(directions)]
    #print(direction)
    if cangotodirection(direction):
        #print("can go to direction")
        gotodirection(direction)
        directionindx +=1
    else:
        gotodirection(directions[directionindx % len(directions)-1])

    if matrix[coord[0],coord[1]] > 265149:
        break

    elem+=1

print(matrix[coord[0],coord[1]])

    #print(matrix)
