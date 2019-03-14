steps = "ne,ne,ne,s,s,s".split(",")
transitions = {("n","s"):"",
            ("s","n"):"",
            ("ne","sw"):"",
            ("sw","ne"):"",
            ("nw","se"):"",
            ("sw","ne"):"",
            ("s","ne"):"se",
            ("ne","s"):"se",
            ("s","nw"):"sw",
            ("nw","s"):"sw",
            ("n","se"):"ne",
            ("se","n"):"ne",
            ("n","sw"):"nw",
            ("sw","n"):"nw",
            ("se","sw"):"s",
            ("ne","nw"):"n"}

complicatedTransitions = {("ne","se","s"):["se","se"],
                          ("nw","sw","s"):["sw","sw"],
                          ("se","ne","n"):["ne","ne"],
                          ("sw","nw","n"):["nw","nw"]
                          }

def reduceSteps():
    for j in range(len(steps)-1):
        for (cord1, cord2) in transitions:
            # print("{} {}".format(inversex,inversey))
            if steps[j] == cord1:
                 if steps[j+1] == cord2:
                     val = transitions.get((cord1, cord2),"NO")
                     if val != "NO" and val != '' :
                         print("changing {} -> {}".format((cord1, cord2),val))
                         steps[j]=val
                         del steps[j+1]
                     elif val == '':
                         del steps[j+1]
                         del steps[j]
                     return True
    return False

def reduceComplicatedSteps():
    for j in range(len(steps)-2):
        for (cord1, cord2, cord3) in complicatedTransitions:
            # print("{} {}".format(inversex,inversey))
            if steps[j] == cord1:
                 # print("a")
                 if steps[j+1] == cord2:
                      # print("b")
                      if steps[j+2] == cord3:
                         # print("c")
                         val = complicatedTransitions.get((cord1, cord2,cord3),"NO")
                         if val != "NO" and val != '' :
                             print("changing {} -> {}".format((cord1, cord2, cord3),val))
                             steps[j]=val[0]
                             steps[j+1]=val[1]
                             del steps[j+2]

                         return True
    return False


print(steps)
while True:
    previousList = list(steps)
    reduceSteps()
    reduceComplicatedSteps()
    print(steps)
    if len(steps) < 1:
        break
    if len(previousList) == len(steps):
        break
