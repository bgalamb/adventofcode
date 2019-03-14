iteration_count = 2017
step_size = 371

def cutAt(array, pos):
    #print("cutting array {} after {} th element".format(array,pos))
    return (array[:pos+1], array[pos+1:])


def extendAt(array,pos,value):
    if len(array) == 1 :
        (p1, p2) = (array,[])
    else:
        (p1, p2) = cutAt(array,pos)
    #print("p1 = {}, p2 = {} , isert val {} at {}".format(p1,p2,value,pos+1))
    return p1 + [value] + p2

spinlock = [0]
position = 0
for i in range(iteration_count):
    # 0 mod 371 = 371
    #print("--->")
    #print("step size {}, position {}".format(step_size, position))
    cut_index = (step_size + position) % len(spinlock)
    position = cut_index

    #print("position {}".format(position))
    spinlock = extendAt(spinlock,cut_index,i+1)
    #print("spinlock {}".format(spinlock))
    cut_index = cut_index+1
    position = position +1
    #print("staying on {}, val={}".format(cut_index,spinlock[cut_index]))

print(spinlock)
