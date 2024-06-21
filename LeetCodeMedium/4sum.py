class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for first in range(n - 3):
            # to allow search space for three more elements after first
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # second should start after first and it is a 3 sum problem from here
                third = second + 1
                fourth = n - 1
                while third < fourth:
                    total = nums[first] + nums[second] + nums[third] + nums[fourth]

                    if total == target:
                        result.append(
                            [nums[first], nums[second], nums[third], nums[fourth]]
                        )
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1

                        third += 1
                        fourth -= 1

                    elif total < target:
                        third += 1
                    else:
                        fourth -= 1
        return result
