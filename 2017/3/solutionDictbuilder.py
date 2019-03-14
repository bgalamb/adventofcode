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
        matrix[(coord[0]+1,coord[1])] = matrix[coord[0],coord[1]] + 1
        coord[0] = coord[0]+1
    #left
    if direction == "left":
        matrix[(coord[0]-1,coord[1])] = matrix[coord[0],coord[1]] + 1
        coord[0] = coord[0]-1
    #up
    if direction == "up":
        matrix[(coord[0],coord[1]+1)] = matrix[coord[0],coord[1]] + 1
        coord[1] = coord[1]+1
    #down
    if direction == "down":
        matrix[(coord[0],coord[1]-1)] = matrix[coord[0],coord[1]] + 1
        coord[1] = coord[1]-1

    #print(matrix)


directionindx = 0
for elem in range(1,6):
    direction = directions[directionindx % len(directions)]
    #print(direction)
    if cangotodirection(direction):
        #print("can go to direction")
        gotodirection(direction)
        directionindx +=1
    else:
        gotodirection(directions[directionindx % len(directions)-1])

    print(matrix)
