arr = [1, 2, 3, 4, 5, 6]
k = 2
def rotate(arr, k):
    k = k % len(arr)
    print(k)
    if len(arr) == 1 or len(arr) == k:
        return arr
    temp = []
    for i in range(k):
        temp.append(arr[i])
    for j in range(len(arr) - k):
        arr[j] = arr[j + k]
    for i in range(len(arr) - k, len(arr)):
        arr[i] = temp[i - k - 1]

rotate(arr, k)
print(arr)