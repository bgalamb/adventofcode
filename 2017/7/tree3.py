filepath = 'input.txt'
tree = dict()
weights = dict()
with open(filepath) as fp:
    for line in fp:
        #line = "fwft (72) -> ktlj, cntj, xhth"
        #line = "pbga (66)"
        parent = line.split("->")[0].split()[0] if len(line.split("->")) > 1 else line.split()[0].strip()
        weight = line.split("->")[0].split()[1][1:-1] if len(line.split("->")) > 1 else line.split()[1].strip()[1:-1]
        children = [elem.strip() for elem in line.split("->")[1].split(",")] if len(line.split("->")) > 1 else []
        tree[parent] = children
        weights[parent] = int(weight)

def weightofnode(node):
    # print("input node {}".format(node))
    val = weights[node]
    # print("val of node {} ".format(val))
    for e in tree[node]:
        # print("child node {}".format(e))
        val += weightofnode(e)
    return val

node = "ltleg"
while True:
    print(weights[node])
    mydict = dict()
    for e in tree[node]:
        print("node {}, weight {} ".format(e,weightofnode(e)))
        mydict[weightofnode(e)].append

    node =
