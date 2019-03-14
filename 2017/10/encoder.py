l = [e for e in range(256)]
# l = [e for e in range(5)]

# inputs = [3, 4, 1, 5]
inputs = [120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113]

def reversesub(l, beginning, length):
    # print("input {}".format(l))
    # print("beginning with {}".format(l[((beginning) % len(l))]))
    templst = []
    for e in range(length):
        templst = templst + [l[((beginning + e) % len(l))]]
    #print("selection {}".format(templst))
    templst.reverse()

    for e in range(length):
        l[((beginning + e) % len(l))] = templst[e]

    #print("output {}".format(l))
    #print("returning {}".format(len(templst)))
    return len(templst)

length = 0
for e in range(len(inputs)):
    #print("offset {}".format(e))
    length += reversesub(l,length,inputs[e])
    length +=e
    #print("[{}]".format(length))
    #print("------")


print(l)
print(l[0]*l[1])
