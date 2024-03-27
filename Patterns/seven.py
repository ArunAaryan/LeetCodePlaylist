rows = 6

for i in range(rows):
    for s in range(rows - i - 1):
        print(" ", end = " ")
    for n in range(2 * i - 1):
        print( "*", end = " ")
    for s in range(rows - i - 1):
        print(" ", end = " ")
    print()

