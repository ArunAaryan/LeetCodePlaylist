def merge(arr, left, right, middle):
    first = left
    second = middle + 1
    L =[]
    R =[]
    while first <= middle:
        L.append(arr[first])
        first += 1
    while second <= right:
        R.append(arr[second])
        second += 1
    first = 0
    second = 0
    current = left
    while first < len(L) and second < len(R):
        if L[first] <= R[second]:
            arr[current] = L[first]
            first += 1
        else:
            arr[current] = R[second]
            second += 1
        current += 1
    while first < len(L):
        arr[current] = L[first]
        first += 1
        current += 1
    while second < len(R):
        arr[current] = R[second]
        second += 1
        current += 1
     
def mergesort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        mergesort(arr, left, middle)
        mergesort(arr, middle + 1, right)
        merge(arr, left, right, middle)
arr = [12, 11, 13, 5, 6, 7]
res = mergesort(arr, 0, len(arr)-1)
print(arr)

