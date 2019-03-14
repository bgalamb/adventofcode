filepath = 'input.txt'
tree = dict()
node = "ahbxz"
# with open(filepath) as fp:
#     for line in fp:
line = "fwft (72) -> ktlj, cntj, xhth"
        #line = "pbga (66)"
parent = line.split("->")[0].split()[0] if len(line.split("->")) > 1 else line.split()[0].strip()
children = [elem.strip() for elem in line.split("->")[1].split(",")] if len(line.split("->")) > 1 else []
for a in children:
    tree[a] = parent

print(tree)
#print(parent)
# print("start node: {}".format(node))

# while True:
#     if tree.get(node,"NotFound") == "NotFound":
#         print("root node: {}".format(node))
#         break;
#     print("current node: {}".format(node))
#     node = tree[node]

#while tree.get(node) is not None:
#    print("current node: {}".format(node))
#    node=tree.get(node)

#print("parent node: {}".format(node))
