from typing import List
class Solution:
    def findDuplicatesSolution1(self, nums: List[int]) -> List[int]:
       unq_set = set([]) 
       dup_list = []
       for num in nums:
           if num in unq_set:
               dup_list.append(num)
           else:
               unq_set.add(num)
       return dup_list

    #random user's solution
    def findDuplicatesSolution2(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) -1] < 0:
                yield num
            else:
                nums[abs(num)-1] *= -1
                
    #naive solution
    def findDuplicatesSolution3(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    print(nums[j])
                    break







s = Solution()
# res = s.findDuplicatesSolution2([1,2,3,2])
s.findDuplicatesSolution3([1,1,2,3,3])

        