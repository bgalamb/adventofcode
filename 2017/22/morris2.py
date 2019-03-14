directions = ["up","right","down","left"] #clockwise
headingindex = 0
heading = directions[0]
infections = 0
lastperformedstep = ""

infected = set()
weakened = set()
flagged = set()

with open("input.txt") as fp:
    numofline = 0
    for line in fp:
        #print(line)
        numofletter = 0
        for letter in line:
            if letter == "#":
                infected.add((numofletter-12,12-numofline))
            numofletter = numofletter + 1
        numofline = numofline + 1




#infected.add((0,0))
standingat = (0,0)
#print("standingat {}".format(standingat))

def step():
    global infections
    global standingat
    global infected
    global weakened
    global flagged
    global heading
    global headingindex
    global lastperformedstep

    if standingat in infected:
        #infected, turn right
        #print("infected")
        headingindex = headingindex + 1
        heading = directions[headingindex % 4]
        #mark as flagged
        infected.remove(standingat)
        flagged.add(standingat)
    elif standingat in weakened:
        #weakened
        #print("weakened")
        weakened.remove(standingat)
        infected.add(standingat)
        infections = infections + 1
        #dont turn directions
    elif standingat in flagged:
        #flagged
        #print("flagged")
        flagged.remove(standingat)
        laststep = lastperformedstep
        was_laststepflagged = True
        if laststep == "up":
            heading = "down"
            headingindex = 2
        if laststep == "down":
            heading = "up"
            headingindex = 0
        if laststep == "left":
            heading = "right"
            headingindex = 1
        if laststep == "right":
            heading = "left"
            headingindex = 3
        #pass
    else:
        #not infected, turn left
        #print("not infected")
        headingindex = headingindex - 1
        heading = directions[headingindex % 4]
        #weken
        weakened.add(standingat)


    #print("heading {}".format(heading))

    #step one
    if heading == "up":
        value = (0,1)
    if heading == "down":
        value = (0,-1)
    if heading == "left":
        value = (-1,0)
    if heading == "right":
        value = (1,0)

    #print("value to add {}".format(value))
    lastperformedstep=heading
    standingat = tuple(map(sum, zip(standingat, value)))

    #print("standingat {}".format(standingat))

def display():
    for j in range(12,-13,-1):
        for i in range(-12,13):
            #print("(i,j) = {},{}".format(i,j))
            if (i,j) == standingat:
                if (i,j) in infected:
                    print("[#]", end='')
                elif (i,j) in weakened:
                    print("[W]", end='')
                elif (i,j) in flagged:
                    print("[F]", end='')
                else:
                    print("[.]", end='')

            elif (i,j) in infected:
                print(" # ", end='')
            elif (i,j) in weakened:
                print(" W ", end='')
            elif (i,j) in flagged:
                print(" F ", end='')
            else:
                print(" . ", end='')
        print("")

i = 0
while i < 10000000:
    #print(i)
    step()
    #print("********")
    #print(infected)
    #print("-------------------------------")
    #display()
    i = i + 1

print("infections {}".format(infections))
