arr = [90,20, 43, 10, 2, 7, 47, 42, 36]

def find(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    small, large = arr[0], arr[0]
    second_small, second_large = float('inf'), -float('inf')
    for i in range(1, len(arr)):
        small = min(small, arr[i])
        large = max(large, arr[i])

    for i in range(len(arr)):
        if arr[i] < second_small  and arr[i] != small:
            second_small =  arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print(second_small, second_large)
find(arr)

