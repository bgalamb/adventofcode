filepath = 'input.txt'
commNetwork = {}
startelem = '0'

with open(filepath) as fp:
    for line in fp:
      (source,target) = line.split(" <-> ")
      target = target.strip().split(", ")
      commNetwork[source] = target

def getGroupForRootNode(rootElem) :
    nodes = [rootElem]
    visited = []
    while len(nodes) > 0:
        nextelem = nodes.pop(0)
        if nextelem in visited :
            continue
        nodes = nodes + commNetwork[nextelem]
        visited = visited + [nextelem]
    return set(visited)

print(len(getGroupForRootNode(startelem)))
