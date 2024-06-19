class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candidate1, candidate2, votes1, votes2 = 0, 0, 0, 0
        # find potential candidates in first pass
        for num in nums:
            if num == candidate1:
                votes1 += 1
            elif num == candidate2:
                votes2 += 1
            elif votes1 == 0:
                candidate1, votes1 = num, 1
            elif votes2 == 0:
                candidate2, votes2 = num, 1
            else:
                votes1 -= 1
                votes2 -= 1
        # find the actual count in pass2
        votes1, votes2 = 0, 0
        result = []
        for num in nums:
            if num == candidate1:
                votes1 += 1
            elif num == candidate2:
                votes2 += 1
        if votes1 > len(nums) // 3:
            result.append(candidate1)
        if votes2 > len(nums) // 3:
            result.append(candidate2)
        return result
