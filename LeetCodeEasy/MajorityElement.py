def majorityElement(arr):
    arr.sort()
    print(arr)
    return arr[len(arr)//2]

    
print(majorityElement([1,2,1,4,2,4,5,2]))