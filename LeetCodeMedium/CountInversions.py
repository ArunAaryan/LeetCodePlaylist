# arr = [1, 2, 3, 4, 5]


def merge_count(arr, left, mid, right, temp):
    i = left
    j = mid + 1
    k = left
    sub_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            sub_count += (
                mid - i + 1
            )  # if current element is greater then arr[j] means all \
            # elements after current element are also greater than j so more inversions
            j += 1
        k += 1
    return sub_count


def merge_sort_count(arr, temp, left, right):
    inversion_count = 0
    if left < right:
        mid = (left + right) // 2

        inversion_count += merge_sort_count(
            arr, temp, left, mid
        )  # divide until one element is left on the left side
        inversion_count += merge_sort_count(
            arr, temp, mid + 1, right
        )  # divide until one element is left on the right side
        inversion_count += merge_count(arr, left, mid, right, temp)
    return inversion_count


def count_inversions(arr):
    n = len(arr)
    temp = [0] * n
    return merge_sort_count(arr, temp, 0, n - 1)


print(count_inversions([1, 2, 3, 4, 5]))
