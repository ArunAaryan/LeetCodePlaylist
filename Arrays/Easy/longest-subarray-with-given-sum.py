k = 10
arr = [2, 3, 5, 1, 1, 1, 1, 1, 5]

# arr = [2, 0, 0, 3]
# k = 3


def findLongestSubArray(arr, k):
    length = max_length = current = 0
    prefix_sum = {}
    for i in range(len(arr)):
        current += arr[i]
        if current == k:  # if adding the current element i contributes to sum
            max_length = max(max_length, i + 1)
        rem = current - k
        if rem in prefix_sum:  # if the current_sum is more than required 'k'
            length = i - prefix_sum[rem]
            max_length = max(max_length, length)

        if current not in prefix_sum:
            # to only store the earliest index; don't store curret one to get max length
            prefix_sum[current] = i

    return max_length


def findLongestSubArrayTwoPointer(arr, k):
    left = right = max_length = 0
    current_sum = arr[0]
    while right < len(arr) - 1:
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        current_sum += arr[right]
    return max_length


res = findLongestSubArrayTwoPointer(arr, k)
print(res)
