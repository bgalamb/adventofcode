registers = {}
operations = []

lastfrekvency = 0

def sndX(X, unused):
    global lastfrekvency
    lastfrekvency = registers[X]
    #print("sndX {}".format(X))
    return 1

def setX(X,Y):
    global registers
    registers[X] = Y if not str(Y).isalpha() else registers.get(Y, 0)
    #print("setX {} {}".format(X,Y))
    return 1

def addX(X,Y):
    global registers
    registers[X] = registers.get(X, 0) + (Y if not str(Y).isalpha() else registers.get(Y, 0))
    #print("addX {} {}".format(X,Y))
    return 1

def mulX(X,Y):
    global registers
    registers[X] = registers.get(X, 0) * (Y if not str(Y).isalpha() else registers.get(Y, 0))
    #print("mulX {} {}".format(X,Y))
    return 1

def modX(X,Y):
    global registers
    registers[X] = registers.get(X, 0) % (Y if not str(Y).isalpha() else registers.get(Y, 0))
    #print("modX {} {}".format(X,Y))
    return 1

def rcvX(X, unused):
    if registers.get(X,0) > 0:
        print("last frekvency {}".format(lastfrekvency))
        quit()
    return 1


def jgzX(X,Y):
    if registers.get(X,0) > 0:
        return Y if not str(Y).isalpha() else registers.get(Y, 0)
    return 1

commands = {
    "snd": sndX,
    "set": setX,
    "add": addX,
    "mul": mulX,
    "mod": modX,
    "rcv": rcvX,
    "jgz": jgzX
}

def createLambda(command_name, x, y):
    return lambda : commands[command_name](x,y)

with open("input.txt") as fp:
    for line in fp:
        splitted_line = line.strip().split()
        cmd = splitted_line[0]
        register_name = splitted_line[1]
        cmd_value = 1
        if len(splitted_line) == 3:
            cmd_value = splitted_line[2]
            if not splitted_line[2].isalpha():
                cmd_value = int(splitted_line[2])

        operations.append(createLambda(cmd, register_name, cmd_value))

currentPosition = 0
print("Starting...")
while True:
    currentPosition += operations[currentPosition]()
