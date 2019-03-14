def getasciiofchar(character):
    return ord(character)

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

def calculatehash(inputs):
    l = [e for e in range(256)]
    for e in range(len(inputs)):
        length = 0
        #print("offset {}".format(e))
        length += reversesub(l,length,inputs[e])
        length +=e
        #print("[{}]".format(length))
        #print("------")
    return l

inputs = [120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113]
# inputchars = ["1","2","3"]
# inputs = [ord(x) for x in inputchars]

print(calculatehash(inputs))
