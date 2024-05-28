# arr = [13,46,24,52,20,9]

arr = [90,20, 43, 10, 2, 7, 47, 42, 36]
for i in range(len(arr)):
    j = i
    while j > 0:
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
print(arr)