rows = 10

for i in range(rows // 2):
    stars = (rows // 2) - i
    spaces = i * 2 
    for j in range(stars):
        print("*", end = " ")
    for s in range(spaces):
        print(" ", end = " ")
    for j in range(stars):
        print("*", end = " ")
    print()
for i in range(rows // 2):
    stars = i + 1
    spaces = (rows - (2 * (i + 1)))
    for j in range(stars):
        print("*", end = " ")
    for s in range(spaces):
        print(" ", end = " ")
    for j in range(stars):
        print("*", end = " ")
    print()
