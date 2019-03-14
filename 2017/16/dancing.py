filepath = 'input.txt'
names = list("abcdefghijklmnop")

def s(st,x):
    #rear part
    st1 = st[:-x]

    #front part
    st2 = st[len(st)-x:]

    return st2+st1

def x(st,a,b):
    elem1 = st[a]
    elem2 = st[b]
    strL = list(st)
    strL[a] = elem2
    strL[b] = elem1
    return "".join(strL)

def  p(st,a,b):
    return x(st,st.index(a),st.index(b))

def createS(x):
    return lambda st: s(st, x)

def createP(a,b):
    return lambda st: p(st,a,b)

def createX(a,b):
    return lambda st: x(st,a,b)

commands = []

with open(filepath) as fp:
    raw_commands = fp.readline().strip().split(",")
    for raw_command in raw_commands:
        commandId = raw_command[0]
        raw_comm_params = raw_command[1:]
        if commandId == "s":
            commands.append(createS(int(raw_comm_params)))
        elif commandId == "p":
            (a, b) = (raw_comm_params.split("/")[0], raw_comm_params.split("/")[1])
            commands.append(createP(a,b))
        elif commandId == "x":
            (a, b) = (raw_comm_params.split("/")[0], raw_comm_params.split("/")[1])
            commands.append(createX(int(a),int(b)))
        else:
            print("wtf")

current = names
previousCommands = set()
for indx in range(10):
    for command in commands:
        current = command(current)
    # if current in previousCommands:
    #     print(indx)
    #     break
    # previousCommands.add(current)

#print(1000000000 % 30)

print(current)
