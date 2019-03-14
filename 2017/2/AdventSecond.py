filepath = 'input.txt'

def minmaxabs(linelist):
    #print(linelist)
    val1 = max(map(int,linelist.split()))
    val2 = min(map(int,linelist.split()))
    return abs(val2-val1)


with open(filepath) as fp:
#fp = ["5 1 9 5"]
#fp = ["104	240	147	246	123	175	372	71	116	230	260	118	202	270	277	292"]
    val = 0
    for line in fp:
      val+=(minmaxabs(line))

print(val)
