rows = 5
A = ord('A')

for i in range(rows):
    for j in range(rows - (i + 1), rows):
        print(chr(A + j), end = " ")
    print()