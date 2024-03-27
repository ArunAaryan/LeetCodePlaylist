# https://takeuforward.org/data-structure/bubble-sort-algorithm/
arr = [13,46,24,52,20,9]

for i in range(len(arr), -1, -1):
    for j in range(i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)