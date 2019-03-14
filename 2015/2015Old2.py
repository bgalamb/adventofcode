def splitter(maxn=5):
 return [[i,maxn-i] for i in range(0,maxn+1)]

def combine(a):
    return sum(map(lambda x: elem[:-1] + x, splitter(elem[-1])) for elem in a)



a = splitter(100)
#print(a)
#print("*******".center(20))
b = combine(a)
#print(b)
#print("*******".center(20))
c=combine(b)
print(len(c))
