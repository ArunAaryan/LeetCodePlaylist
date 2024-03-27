A = ord('A')
rows = 4
for i in range(rows):
    for s in range(rows - i - 1):
        print(" ", end = "")
    for j in range(0,  (2 * i) + 1 ):
        if(j <= (2 * i) / 2):
            print(chr(A + j), end = "") 
        else:
            print(chr(A + (2 * i) - j), end = "")
    for  s in range(rows - i - 1):
        print(" ", end = "")
    
    print( )