memory = [5,1,	10,	0,	1,7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]
#memory = [0,2,7,0]
#memory = [2,4,1,2]
#memory = [0,2,2,0]

def performmemrealloc(memory):
    minindex = memory.index(max(memory))
    maxelem = memory.pop(minindex)
    #print("input {}".format(memory))


    integers = maxelem // len(memory)
    remaining = maxelem % len(memory)

    if integers > 0:
        memory = [elem + integers for elem in memory]
        memory.insert(minindex, remaining)
    else:
        for e in range(remaining):
            myindex = (minindex + e) % len(memory)
            memory[myindex] = memory[myindex] + 1
        memory.insert(minindex,0)

    return(memory)

resultset = []
i=0
while True:
    i+=1
    memory = (performmemrealloc(memory))
    if tuple(memory) not in resultset:
        resultset.append(tuple(memory))
    else:
        j = resultset.index(tuple(memory))
        print("number of iteration: {}, cycle length: {}".format(i, i-j-1))
        break
