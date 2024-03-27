rows = 5

for i in range(rows):
    for p in range(i + 1):
        print("*", end = " ")
    print()
for i in range(rows):
    for p in range(rows - (i + 1)):
        print("*", end = " ")
    print()