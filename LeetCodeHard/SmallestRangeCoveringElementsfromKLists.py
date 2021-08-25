from heapq import heapify, heappop, heappush
class Solution:
    def smallestRange(self, nums):
        heap = []
        for row, val in enumerate(nums):
            heap.append((val[0], row, 0)) 
        heapify(heap)
        right = max(row[0] for row in nums) #initial right, select the largest number from every row's first index
        ans = (-float('inf'), float('inf'))
        while heap:
            left, row, col = heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if col + 1 == len(nums[row]): # if any row has already reached the end, return ans
                return ans
            next_element = nums[row][col + 1] 
            right = max(right, next_element)
            heappush(heap, (next_element, row, col + 1))

s = Solution()
res = s.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
print(res) 
        