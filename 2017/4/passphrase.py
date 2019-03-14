filepath = 'input.txt'

def validate(words):
    for indx1, elem in enumerate(words):
        for indx2, duplicate in enumerate(words):
            if indx2 != indx1:
                firstChars = set(chars for chars in elem)
                duplicateChars = set(chars for chars in duplicate)

                if firstChars == duplicateChars:
                    #print("found")
                    return 0
    #print(1)
    return 1

i = 0
with open(filepath) as fp:
#fp = ["aba bb cc dd aab"]
    val=0
    for line in fp:
      #print(line)
      i += 1
      words = line.split()
      val+=(validate(words))

print(i)
print(val)
