filepath = 'input.txt'

def validate(words):
    for indx1, elem in enumerate(words):
        for indx2, duplicate in enumerate(words):
            if indx2 != indx1:
                if elem == duplicate:
                    return(0)
    #print(1)
    return 1

i = 0
with open(filepath) as fp:
#fp = ["aa bb cc dd aa"]
    val=0
    i += i+1
    for line in fp:
     print(line)
     words = line.split()
     val+=(validate(words))

    print(i)
    print(val)
