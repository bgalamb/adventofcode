
queue0 = []
queue1 = []
counter = 0

class DuetProcess:



        def __init__(self,programId):
             self.registers = {}
             self.operations = []
             self.currentPosition = 0
             self.programId=programId
             self.registers["p"] = programId

             self.commands = {
                 "snd": self.sndX,
                 "set": self.setX,
                 "add": self.addX,
                 "mod": self.modX,
                 "mul": self.mulX,
                 "rcv": self.rcvX,
                 "jgz": self.jgzX,
             }

             #print("Init self.programId {}".format(self.programId))
             with open("input.txt") as fp:
                 for line in fp:
                     splitted_line = line.strip().split()
                     cmd = splitted_line[0]
                     register_name = splitted_line[1]
                     if not register_name.isalpha():
                         register_name = int(register_name)
                     cmd_value = 1
                     if len(splitted_line) == 3:
                         cmd_value = splitted_line[2]
                         if not splitted_line[2].isalpha():
                             cmd_value = int(splitted_line[2])

                     self.operations.append(self.createLambda(cmd, register_name, cmd_value))

        def createLambda(self, command_name, x, y):
            return lambda : self.commands[command_name](x,y)

        def sndX(self, X, unused):
            global queue0
            global queue1
            #print("{} process sndX {}".format(self.programId,X) )
            if self.programId == 0 :
                queue1.append(X if not str(X).isalpha() else self.registers.get(X, 0))
            else :
                global counter
                counter = counter + 1
                print(counter)
                queue0.append(X if not str(X).isalpha() else self.registers.get(X, 0))
            return 1

        def setX(self,X,Y):
            self.registers[X] = Y if not str(Y).isalpha() else self.registers.get(Y, 0)
            #print("{} process setX {} {}".format(self.programId,X,Y))
            return 1

        def addX(self,X,Y):
            self.registers[X] = self.registers.get(X, 0) + (Y if not str(Y).isalpha() else self.registers.get(Y, 0))
            #print("{} process addX {} {}".format(self.programId,X,Y))
            return 1

        def mulX(self,X,Y):
            self.registers[X] = self.registers.get(X, 0) * (Y if not str(Y).isalpha() else self.registers.get(Y, 0))
            #print("{} process mulX {} {}".format(self.programId,X,Y))
            return 1

        def modX(self,X,Y):
            self.registers[X] = self.registers.get(X, 0) % (Y if not str(Y).isalpha() else self.registers.get(Y, 0))
            #print("{} process modX {} {}".format(self.programId,X,Y))
            return 1

        def rcvX(self,X,unused):
            #print("{} process rcvX {}".format(self.programId,X))
            global queue0
            global queue1
            if self.programId == 0 :
                if len(queue0) > 0 :
                    self.registers[X] = queue0[0]
                    queue0 = queue0[1:]
                    return 1
            else:
                if len(queue1) > 0 :
                    self.registers[X] = queue1[0]
                    queue1 = queue1[1:]
                    return 1

            #print("{} waiting for element in the input queue".format(self.programId))
            return 0

        def jgzX(self,X,Y):
            #print("{} process jgzX {}".format(progID,X))
            value = X
            if not str(X).isalpha():
                value = int(value)
            else:
                value = self.registers.get(X, 0)

            if value > 0:
                return Y if not str(Y).isalpha() else self.registers.get(Y, 0)
            return 1

        def printOprX(self):
             print(self.operations)

        def printRegX(self):
             print("{} {}".format(self.programId,self.registers))

        def printQueueX(self):
            if self.programId == 0 :
                print("{} - {}".format(self.programId,queue0))
            else :
                print("{} - {}".format(self.programId,queue1))

        def runStep(self):
            #print("{} running next step -----------".format(self.programId))
            self.currentPosition += self.operations[self.currentPosition]()
            #self.printRegX()
            #self.printQueueX()

DuetProcess0 = DuetProcess(0)
DuetProcess1 = DuetProcess(1)


print("*************")
# i=0
while True:
    DuetProcess0.runStep()
    DuetProcess1.runStep()
    # DuetProcess0.printQueueX()
    # DuetProcess1.printQueueX()
    # DuetProcess0.printRegX()
    # DuetProcess1.printRegX()
    # i = i+1
