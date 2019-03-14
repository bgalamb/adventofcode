filepath = 'input.txt'

def maxdivid(linelist):
    #print(linelist)
    val1 = map(int,linelist.split())
    for indx, elem in enumerate(val1):
        for indx2, elem2 in enumerate(val1):
            if indx != indx2:
                if elem%elem2 == 0:
                    print (elem,elem2)
                    return int(elem/elem2)

with open(filepath) as fp:
#fp = ["3 8 6 5"]
#fp = ["104	240	147	246	123	175	372	71	116	230	260	118	202	270	277	292"]
 val = 0
 for line in fp:
   val+=(maxdivid(line))

 print(val)
