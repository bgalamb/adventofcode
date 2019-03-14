filepath = "input.txt"

def performsteps(inputlist):
    index = 0
    i = 0
    while True:
        oldindex = index
        oldval = inputlist[index]
        index  = inputlist[index]+oldindex
        inputlist[oldindex] = oldval + 1
        #print("*******************".center(50))
        #print((inputlist,index))
        i += 1
        if((index > len(inputlist)-1) or index<0):
            return i

vals =[]

with open(filepath) as fp:
 for line in fp:
   vals.append(int(line.strip()))

print(vals)

print(performsteps(vals))
