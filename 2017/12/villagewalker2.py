filepath = 'input.txt'
commNetwork = {}

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

subgraphs = []

for e in commNetwork:
    currentSubgraph = getGroupForRootNode(e)
    for subgraph in subgraphs:
        if currentSubgraph.issubset(subgraph):
            #print("current graph aready exists, break")
            break
    else:
        for subgraph in subgraphs:
            if subgraph.issubset(currentSubgraph):
                print("removing a smaller graph from all subgraphs")
                subgraphs.remove(subgraph)
            #print("added subgraph as it dit not exist")
        else:
            subgraphs.append(currentSubgraph)

print(len(subgraphs))
