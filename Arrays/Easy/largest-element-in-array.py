arr = [90,20, 43, 10, 2, 7, 47, 42, 36]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)