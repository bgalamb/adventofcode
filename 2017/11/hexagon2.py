import operator

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \


steps = "n,ne,ne,ne,se,s,s,ne,s,nw,nw,sw,n,sw,sw".split(",")
koord = (1,3)

possible = ["n","s","ne","nw","se","sw"]

def performstep(step):
    global koord
    print(koord)
    isEven = koord[0] % 2 == 1
    print("current step {} on coordinate {}".format(step,koord))
    if step == "n" : koord= tuple(map(operator.add,koord,(0,-1)))
    if step == "s" : koord= tuple(map(operator.add,koord,(0,1)))
    if step == "ne": koord= tuple(map(operator.add,koord,(1,0)))   if isEven else tuple(map(operator.add,koord,(1,-1)))
    if step == "nw": koord= tuple(map(operator.add,koord,(-1,0)))  if isEven else tuple(map(operator.add,koord,(-1,-1)))
    if step == "se": koord= tuple(map(operator.add,koord,(1,0)))   if not isEven else tuple(map(operator.add,koord,(1,1)))
    if step == "sw": koord= tuple(map(operator.add,koord,(-1,0)))  if not isEven else tuple(map(operator.add,koord,(-1,1)))
    print("new coordinate {}".format(koord))

for step in steps:
    performstep(step)
