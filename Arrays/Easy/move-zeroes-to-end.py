arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
arr = [ 1,2,0,1,0,4,0]
def leftRotate(arr, start, end):
    temp = arr[start]
    while start < end:
        arr[start] = arr[start + 1]
        start += 1
    arr[end] = temp

def moveZeroes(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] == 0:
            leftRotate(arr, start, end)
        start += 1
    

# moveZeroes(arr)

def moveZeroesTwoPointer(arr):
    z = len(arr)
    for i in range(len(arr)):
        if not arr[i]:
            z = i
            break
    if z == len(arr):
        return 
    
    nz = z + 1
    while nz < len(arr):
        if arr[nz]:
            arr[z], arr[nz] = arr[nz], arr[z]
            z += 1
        nz += 1
moveZeroesTwoPointer(arr)
print(arr)




    
