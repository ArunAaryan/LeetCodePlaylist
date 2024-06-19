def majorityElement(arr):
    arr.sort()
    print(arr)
    return arr[len(arr) // 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting algorithm
        candidate, votes = nums[0], 0
        for i in range(len(nums)):
            if not votes:
                candidate = nums[i]
            if nums[i] == candidate:
                votes += 1
            else:
                votes -= 1

        return candidate


print(majorityElement([1, 2, 1, 4, 2, 4, 5, 2]))
