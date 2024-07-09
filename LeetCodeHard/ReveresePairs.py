class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # create a temp array to keep the track of original array elements because we are modifying\
        # the original array
        temp = [0] * len(nums)
        return self.merge_sort(nums, temp, 0, len(nums) - 1)

    def merge_sort(self, nums, temp, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        count = 0
        count += self.merge_sort(nums, temp, left, mid)
        count += self.merge_sort(nums, temp, mid + 1, right)
        count += self.merge(nums, temp, left, mid, right)
        return count

    def merge(self, nums, temp, left, mid, right):
        # copy the sub array structure into temp; as we modify the original array
        for i in range(left, right + 1):
            temp[i] = nums[i]

        i, j = left, mid + 1
        count = 0
        # count the elements that meet the condition
        while i <= mid:
            while j <= right and nums[i] > nums[j] * 2:
                j += 1
            count += j - (mid + 1)
            i += 1

        # merge the sub arrays
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
            k += 1
        while i <= mid:
            nums[k] = temp[i]
            i += 1
            k += 1
        while j <= right:
            nums[k] = temp[j]
            j += 1
            k += 1
        return count
