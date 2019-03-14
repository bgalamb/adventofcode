#(generator A uses 16807; generator B uses 48271), and then keep the remainder of dividing that resulting product by 2147483647.
#That final remainder is the value it produces next.

def generate(firstElem, multiplier,condition = lambda _: True):
    current = firstElem
    while True:
        current = (current * multiplier) % 2147483647
        if condition(current):
            yield current

def concat(a, b):
    while True:
        yield (a.next(), b.next())

counter = 0
judge = 0
for i,j in concat(generate(783, 16807, lambda c: c % 4 == 0), generate(325, 48271, lambda c: c % 8 == 0)):
    # print("{}, {:2b}".format(i,i))
    # print("{}, {:2b}".format(j,j))
    if "{:2b}".format(i)[-16:] == "{:2b}".format(j)[-16:] :
        judge = judge + 1

    counter = counter + 1
    if counter >= 5000000: #40000000 for part 1.
         print judge
         break
