arr = [ 2, 7, 7, 10, 10, 20,  36, 42, 42, 43, 47, 90, 90]

def remove_duplicates(arr):
    if len(arr) == 1:
        return arr

    i = 0
    for  j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]
            i += 1

    
remove_duplicates(arr)
print(arr)