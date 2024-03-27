A = ord('A')
rows = 5

for i in range(rows , 0, -1):
    for j in range(i):
        print(chr(A + j), end = " ")
    print()
