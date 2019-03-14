#input1 = "..^^."
#input1 = ".^^.^.^^^^"
input1 = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
current = input1


#  |X        |
# .|...^^.^..|.
def calctraps(currentline):
    newline = ""
    for idx in range(1, len(currentline)-1):
        vals = currentline[idx - 1: (idx-1) + 3]
        newline += "." if not isTrap(vals) else "^"
        #print("values {}".format(vals))
    return newline

def isTrap(vals):

    # Its left and center tiles are traps, but its right tile is not.
    if vals[0] == "^" and vals[1] == "^" and vals[2] == ".":
        return True
    # Its center and right tiles are traps, but its left tile is not.
    if vals[0] == "." and vals[1] == "^" and vals[2] == "^":
        return True
    # Only its left tile is a trap.
    if vals[0] == "^" and vals[1] == "." and vals[2] == ".":
        return True
    # Only its right tile is a trap.
    if vals[0] == "." and vals[1] == "." and vals[2] == "^":
        return True
    return False


safetiles = len(list(filter(lambda x: x == ".", current)))
for i in range(39):
    current = calctraps("." + current + ".")
    safetiles += len(list(filter(lambda x: x == ".", current)))
    print(current)

print(safetiles)
