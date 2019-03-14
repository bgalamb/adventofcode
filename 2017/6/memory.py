memory = [5,1,	10,	0,	1,7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]
#memory = [0,2,7,0]
#memory = [2,4,1,2]
#memory = [0,2,2,0]
# print(memory)
i=0


def performmemrealloc(memory):
    minindex = 0
    maxelem = 0
    #print("input : {}".format(memory))
    for indx, elem in enumerate(memory):
        if indx == 0 :
            minidex = indx
            maxelem = elem
        else:
            #print((indx, elem, maxelem,elem > maxelem))
            if elem > maxelem:
                maxelem = elem
                minindex = indx

    memory.pop(minindex)
    integers = maxelem // len(memory)
    remaining = maxelem % len(memory)
    memory = [elem + integers for elem in memory]

    if integers > 0:
        memory.insert(minindex, remaining)
    else:
        for e in range(remaining):
            myindex = (minindex + e) % len(memory)
            #print("myindex {}".format(myindex))
            memory[myindex] = memory[myindex] + 1
        memory.insert(minindex,0)

    #print(memory)
    return(memory)



resultset = []
while True:
    memory = (performmemrealloc(memory))
    #print("output : {}".format(memory))
    if tuple(memory) not in resultset:
        resultset.append(tuple(memory))
    else:
        break
    #print("Iteration times {}".format(i))
    #print("output {}".format(resultset))
    i+=1

print("memory {}".format(memory))
print(i+1)

for idx, elem in enumerate(resultset):
    if elem == tuple(memory):
        print(idx)
        break

#3955
#5042
print(i-idx)
