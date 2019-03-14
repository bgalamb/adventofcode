initvalue = ".#./..#/###"
rules = {}

def illustrate(input1):
    lines = input1.split("/")
    for line in lines:
        print(line)
    print("----------------")

#  #.  ->  ##
#  #.  ->  ..
def rotate(input1):
    lines = input1.split("/")
    if len(lines) == 3 :
        return lines[2][0]+lines[1][0]+lines[0][0] + "/" + \
               lines[2][1]+lines[1][1]+lines[0][1] + "/" + \
               lines[2][2]+lines[1][2]+lines[0][2]

    if len(lines) == 2 :
        return lines[0][1]+lines[1][1] + "/" + \
               lines[0][0]+lines[1][0]

def flipHorizontal(input1):
    lines = input1.split("/")
    if len(lines) == 3 :
        return lines[0][::-1] + "/" + \
               lines[1][::-1] + "/" + \
               lines[2][::-1]
    if len(lines) == 2 :
        return lines[0][::-1] + "/" + \
               lines[1][::-1]

def flipVertical(input1):
    lines = input1.split("/")
    if len(lines) == 3 :
        return lines[2] + "/" + \
               lines[1] + "/" + \
               lines[0]
    if len(lines) == 2 :
        return lines[1] + "/" + \
               lines[0]

def breakup(input1):
    result = []
    lines = input1.split("/")

    if len(lines) % 2 == 0:
        division = len(lines) // 2
        rowOffset = 0
        for e in range(division):
            columnOffset = 0
            for j in range(division):
                value = ""
                for h in range(2):
                    for k in range(2):
                        # print("h {}".format(h))
                        # print("k {}".format(k))
                        # print("rowOffset {}".format(rowOffset))
                        # print("columnOffset {}".format(columnOffset))
                        value += lines[h + rowOffset][k + columnOffset]
                    value += "/"
                result.append(value[:-1])
                columnOffset += 2
            rowOffset += 2
    elif len(lines) % 3 == 0:
        #fix this
        division = len(lines) // 3
        rowOffset = 0
        for e in range(division):
            columnOffset = 0
            for j in range(division):
                value = ""
                for h in range(3):
                    for k in range(3):
                        # print("h {}".format(h))
                        # print("k {}".format(k))
                        # print("rowOffset {}".format(rowOffset))
                        # print("columnOffset {}".format(columnOffset))
                        value += lines[h + rowOffset][k + columnOffset]
                    value += "/"
                result.append(value[:-1])
                columnOffset += 3
            rowOffset += 3
    else:
        result = [input1]
    print("breaking up to pieces...")
    return result

# pieces: ['#./..', '.#/..', '../#.', '../.#']
# pieces: ['##./#../...', '##./#../...', '##./#../...', '##./#../...']
# result: '#..#/..../..../#..#'
def mergepieces(inputArr):
    result = ""
    outerdimension = int(len(inputArr)**(.5))
    innerdimension = len(inputArr[0].split("/")[0])

    pieceses = []
    for elem in range(0, len(inputArr), outerdimension):
          pieceses.append(inputArr[elem : elem + outerdimension])
    #print("pieceses {}".format(pieceses))
    for outerrow in range(outerdimension):
        for innerrow in range(innerdimension):
            for outercolumn in range(outerdimension):
                 #print("outerrow {}, outercolumn {}, innerrow {}, pieceses[outerrow] {}".format(outerrow,outercolumn,innerrow,pieceses[outerrow]))
                 #print(pieceses[outerrow][outercolumn].split("/")[innerrow])
                 result += pieceses[outerrow][outercolumn].split("/")[innerrow]
            result += "/"
    print("merging results...")
    return result[:-1]

with open("input.txt") as fp:
    for line in fp:
        rulekey = line.split("=>")[0].strip()
        rulevalue = line.split("=>")[1].strip()
        rules[rulekey] = rulevalue
        for _ in range(8):
            rulekey = rotate(rulekey)
            rules[rulekey]=rulevalue
            rules[flipHorizontal(rulekey)]=rulevalue
            rules[flipVertical(rulekey)]=rulevalue

def applyrulefor(input1):
    #print("applied rules...")
    return rules.get(input1, input1)

#print(rules)

i = 0
value = initvalue
illustrate(value)
while i < 5:
    print("iteration {}".format(i))
    value = applyrulefor(value)
    illustrate(value)

    broken = breakup(value)
    #print("broken {}".format(broken))
    brokemodified = []

    for elem in broken:
         brokemodified.append(applyrulefor(elem))
    #print("brokenmodified {}".format(brokemodified))

    value = mergepieces(brokemodified)
    illustrate(value)
    print("counting light = {}".format(value.count("#")))
    i = i + 1
