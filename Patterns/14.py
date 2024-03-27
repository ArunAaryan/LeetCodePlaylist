rows = 5

A = 65
for i in range(rows + 1):
    for j in range(i):
        print(chr(A + j), end = " ")
    print()