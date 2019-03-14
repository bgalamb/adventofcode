pathmap = []

linenum = 0
with open("input.txt") as fp:
    for line in fp:
        pathmap.append(line.rstrip('\n'))

headings = ["down","up","left","right"]

def getEntryElement():
    indx = 0
    for e in pathmap[0]:
        if e == "|":
            print("First {}".format((0,indx)))
                   # x, y, value, heading
            return (0,indx,"down",pathmap[0][indx]) #down, up, left, right
        indx = indx + 1

def getNextElemDown(coordinate):
    #print("nextElemDown")
    if len(pathmap[coordinate[0]+1]) < coordinate[1]+1 :
        return (coordinate[0]+1,coordinate[1],"down"," ")
    return (coordinate[0]+1,coordinate[1],"down",pathmap[coordinate[0]+1][coordinate[1]])

def getNextElemUp(coordinate):
    #print("nextElemUp")
    if len(pathmap[coordinate[0]-1]) < coordinate[1]+1:
        return (coordinate[0]-1,coordinate[1],"up"," ")
    return (coordinate[0]-1,coordinate[1],"up",pathmap[coordinate[0]-1][coordinate[1]])

def getNextElemLeft(coordinate):
    #print("nextElemLeft")
    if len(pathmap[coordinate[0]]) < coordinate[1]+1-1:
        return (coordinate[0],coordinate[1],"left"," ")
    return (coordinate[0],coordinate[1]-1,"left",pathmap[coordinate[0]][coordinate[1]-1])

def getNextElemRight(coordinate):
    #print("nextElemRight")
    if len(pathmap[coordinate[0]]) < coordinate[1]+1+1:
        return (coordinate[0],coordinate[1],"right"," ")
    return (coordinate[0],coordinate[1]+1,"right",pathmap[coordinate[0]][coordinate[1]+1])


def getNextElement(coordinate):
    if coordinate[2] == "down":
        nextElem = getNextElemDown(coordinate)
        #print("nextElem {}".format(nextElem))
        if nextElem[0] < 0 or nextElem[1] < 0:
            quit()
        if nextElem[3] == "+":
            return getNextElemRight(nextElem) if getNextElemRight(nextElem)[3] != " " else getNextElemLeft(nextElem)
        elif nextElem[3] == " " :
            quit()
        else:
            return nextElem
    if coordinate[2] == "up":
        nextElem = getNextElemUp(coordinate)
        #print("nextElem {}".format(nextElem))
        if nextElem[0] < 0 or nextElem[1] < 0:
            quit()
        if nextElem[3] == "+":
            return getNextElemRight(nextElem) if getNextElemRight(nextElem)[3] != " " else getNextElemLeft(nextElem)
        elif nextElem[3] == " " or nextElem[0] < 0 or nextElem[1] < 0 :
            quit()
        else:
            return nextElem
    if coordinate[2] == "left":
        nextElem = getNextElemLeft(coordinate)
        #print("nextElem {}".format(nextElem))
        if nextElem[0] < 0 or nextElem[1] < 0:
            quit()
        if nextElem[3] == "+":
            return getNextElemUp(nextElem) if getNextElemUp(nextElem)[3] != " " else getNextElemDown(nextElem)
        elif nextElem[3] == " " or nextElem[0] < 0 or nextElem[1] < 0 :
            quit()
        else:
            return nextElem
    if coordinate[2] == "right":
        nextElem = getNextElemRight(coordinate)
        #print("nextElem {}".format(nextElem))
        if nextElem[0] < 0 or nextElem[1] < 0:
            quit()
        if nextElem[3] == "+":
            return getNextElemUp(nextElem) if getNextElemUp(nextElem)[3] != " " else getNextElemDown(nextElem)
        elif nextElem[3] == " " or nextElem[0] < 0 or nextElem[1] < 0 :
            quit()
        else:
            return nextElem

firstelement = getEntryElement()
nxtElem = getNextElement(firstelement)
i = 0
while True:
    nxtElem = getNextElement(nxtElem)
    if nxtElem[3].isalpha():
        print nxtElem
    i = i +1
