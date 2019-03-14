filename = "input.txt"
result = ""
result2 = 0


level = 0
totalgarbage = 0
currgarbage = 0

with open(filename) as f:
  garbagestart = False
  skipnext = False
  temp = ""

  while True:
    c = f.read(1)
    if not c :
        break
    if skipnext:
        skipnext = False
        continue
    elif c == '!':
        skipnext = True
        continue
    elif c == '<' and not garbagestart:
        garbagestart = True
        continue

    elif c == '>' and garbagestart:
        garbagestart = False
        totalgarbage += currgarbage
        currgarbage = 0
        continue

    elif not garbagestart:
        if c == "{":
            level += 1
            result+=" "+str(level)
            result2+=level
        elif c == "}":
            level -= 1
        elif c == ",":
            continue
    elif garbagestart:
        currgarbage+=1


#print(result)
print(result2)
print("garbage {}".format(totalgarbage))
