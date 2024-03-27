# https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/

arr = [13,46,24,52,20,9]

for i in range(0, len(arr)):
    smallest = arr[i] 
    for j in range(i + 1, len(arr)):
        if arr[j] < smallest:
            smallest = arr[j]
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
        
    

