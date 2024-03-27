rows = 5

flip = 1
for i in range(rows):
    if (i % 2 == 0):
        flip = 1
    else:
        flip = 0
    for j in range(i + 1):
        print(flip, end = " ")
        flip = 1 - flip

    print()
    
