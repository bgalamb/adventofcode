buildingblocks = []

with open("input.txt") as fp:
    for line in fp:
        line2 = line.strip()
        vals = line2.split("/")
        buildingblocks.append((int(vals[0]),int(vals[1])))

#buildingblocks = [(0,1),(0,1),(1,1),(1,2),(1,3),(1,4),(2,1)]
print(buildingblocks)
firstelement = 0
allfinalbridges = []
bridge = []

def findMatchingConnectors(base, connectors):
    matching = filter(lambda x: x[0] == base or x[1] == base, connectors)
    #sortedd = map(lambda x: (x[0], x[1]) if x[0] == base else (x[1], x[0]), matching)
    return list(matching)

def strenght(bridge):
    result = 0
    for elem in bridge:
        result = result + elem[0] + elem[1]
    return result

def buildbridge(inconnector,inbuildingblocks,inbridge,allbridges): # [[(Int, Int)]]
    #print("buildbridge called with connector= {}, buildingblocks= {}, bridge= {}, allbridges= {}".format(inconnector,inbuildingblocks,inbridge,allbridges))
    foundconnectors = findMatchingConnectors(inconnector,inbuildingblocks)

    #append a new bridge to the list of bridges
    if len(foundconnectors) == 0:
         allbridges.append(inbridge)

    for connector in foundconnectors:
        #create new instances
        newbuildingblocks = list(inbuildingblocks)
        newbridge = list(inbridge)

        #append to the bridge the new connector element
        newbridge.append(connector)

        #remove the connector element from the available list
        newbuildingblocks.remove(connector)
        if inconnector == connector[0]:
            buildbridge(connector[1],newbuildingblocks,newbridge,allbridges)
        else :
            buildbridge(connector[0],newbuildingblocks,newbridge,allbridges)

    return allbridges

allbridg = buildbridge(firstelement,buildingblocks,bridge,allfinalbridges)

#print(allbridg)
maxstrength = 0
strenghtVal = 0
for a in allbridg:
    #print("bridge = {}".format(a))
    strenghtVal = strenght(a)
    #print("strength= {}".format(strenghtVal))
    if strenghtVal > maxstrength:
        maxstrength = strenghtVal

print maxstrength
