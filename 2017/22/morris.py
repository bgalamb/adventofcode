directions = ["up","right","down","left"] #clockwise
headingindex = 0
heading = directions[0]
infections = 0

infected = set()

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
    global heading
    global headingindex
    if standingat in infected:
        #infected, turn right
        #print("infected")
        headingindex = headingindex + 1
        heading = directions[headingindex % 4]
        #desinfect
        infected.remove(standingat)
    else:
        #not infected, turn left
        #print("not infected")
        headingindex = headingindex - 1
        heading = directions[headingindex % 4]
        #infect
        infected.add(standingat)
        infections = infections + 1

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
    standingat = tuple(map(sum, zip(standingat, value)))

    #print("standingat {}".format(standingat))


i = 0
while i < 10000:
    step()
    #print("********")
#print(infected)
    i = i + 1

print("infections {}".format(infections))
