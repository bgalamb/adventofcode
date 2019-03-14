import operator
filepath = 'input.txt'


#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
#steps = "n,ne,ne,ne,se,s,s,ne,s,nw,nw,sw,n,sw,sw".split(",")

def performstep(location,step):
    #print(location)
    newlocation = 0
    isEven = location[0] % 2 == 1
    #print("current step {} on coordinate {}".format(step,location))
    if step == "n" : newlocation= tuple(map(operator.add,location,(0,-1)))
    if step == "s" : newlocation= tuple(map(operator.add,location,(0,1)))
    if step == "ne": newlocation= tuple(map(operator.add,location,(1,0)))   if isEven else tuple(map(operator.add,location,(1,-1)))
    if step == "nw": newlocation= tuple(map(operator.add,location,(-1,0)))  if isEven else tuple(map(operator.add,location,(-1,-1)))
    if step == "se": newlocation= tuple(map(operator.add,location,(1,0)))   if not isEven else tuple(map(operator.add,location,(1,1)))
    if step == "sw": newlocation= tuple(map(operator.add,location,(-1,0)))  if not isEven else tuple(map(operator.add,location,(-1,1)))

    #print("new coordinate {}".format(newlocation))
    return newlocation


def isIncolumn(originalcoord,currentkoord):
    if originalcoord[0] == currentkoord[0]:
        return True
    else:
        return False

def isInRow(originalcoord,currentcoord):
    if originalcoord[1] == currentkoord[1]:
        return True
    else:
        return False


def isInRow(originalcoord,coord):
    if originalcoord[1] - coord[1] == 0:
        #print("{} and {} are in the same row".format(originalcoord,coord))
        return True


def isInColumn(originalcoord,coord):
    if originalcoord[0] - coord[0] == 0:
        #print("{} and {} are in the same column".format(originalcoord,coord))
        return True


def calculatedistane(coord,originalcoord):
    distance = 0

    while True:
        if isInRow(originalcoord,coord):
            return distance + abs(originalcoord[0]-coord[0])
        if isInColumn(originalcoord,coord):
            return distance + abs(originalcoord[1]-coord[1])

        #is to the right
        if originalcoord[0] - coord[0] < 0 :
            #is down
            if originalcoord[1] - coord[1] < 0 :
                originalcoord=performstep(originalcoord,"se")
            #is up
            else:
                originalcoord=performstep(originalcoord,"ne")
        #is to the right
        else:
            #is down
            if originalcoord[1] - coord[1] < 0 :
                originalcoord=performstep(originalcoord,"sw")
            #is up
            else:
                originalcoord=performstep(originalcoord,"nw")

        distance = distance + 1

    return distance

coord = (0,0)
originalcoord = (0,0)
coords = []
distances = []

with open(filepath) as fp:
    for line in fp:
     steps = line.strip().split(",")

for step in steps:
    coord = performstep(coord,step)
    distances.append(calculatedistane(coord,originalcoord))

print(max(distances))
