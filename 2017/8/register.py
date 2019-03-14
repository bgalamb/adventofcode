import operator

filepath = 'input.txt'

ls = "<"
gr = ">"
eq = "=="
lseq = "<="
greq = ">="
neq = "!="

inc = "inc"
dec = "dec"

vals = dict()

def command(a,b,operator):
    print("->[{}], [{}], [{}]".format(a,operator,b))
    if operator == inc:
        return  a+b
    else:
        return  a-b

def condition(a,b,condition):
    print("[{}], [{}], [{}] ??".format(a,condition,b))
    if condition == ls:
        return a < b
    elif condition == lseq:
        return a <= b
    elif condition == gr:
        return a > b
    elif condition == greq:
        return a >= b
    elif condition == neq:
        return a != b
    else :
        return a==b

maxn = 0
with open(filepath) as fp:
 for line in fp:
    #line = "b inc 5 if a < 1"
    comm = line.split()
    if condition(int(vals.get(comm[4],0)),int(comm[6],0),comm[5]):
        #print("condition is true")
        vals[comm[0]] = command(int(vals.get(comm[0],0)),int(comm[2]),comm[1])

        if vals[comm[0]] > maxn:
            maxn = vals[comm[0]]
    #print(vals)

print("greatest value {}".format(max(vals.iteritems(), key=operator.itemgetter(1))))
print("maximum value ever {}".format(maxn))
