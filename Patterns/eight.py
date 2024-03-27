rows = 5

for i in range(rows):
    for s in range(i):
        print(" ", end = " ")
    for n in range(2 * (rows - i) - 1):
        print("*" , end = " ")
    for s in range(i):
        print(" ", end = "")
    print()
    