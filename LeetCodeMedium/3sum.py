class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        #sort eliminates duplicate results
        # need to make one element fixed and keep one element from fixed + 1 and other from end towards left
        for fixed in range(len(nums) - 2): # -2 because 2 elements first and second
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:#skip duplicate fixed value
                continue
            second = fixed + 1
            third = len(nums) - 1
            while second < third:
                total = nums[fixed] + nums[second] + nums[third]
                if total < 0: # got negative value then move second towards right
                    second += 1
                elif total > 0: # positive so reduce the right pointer
                    third -= 1
                else: # got exactly 0 
                    res.append([nums[fixed], nums[second], nums[third]])
                    # skip duplicate second values from left
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    #skip duplicate third values from right
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    # reduce the search space from left and right
                    second += 1
                    third -= 1
        return res


    #some best solution : https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        positives = [] 
        negatives =[]
        zeros = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros.append(num)
        P_set = set(positives)
        N_set = set(negatives)
        print('positives',positives)
        print(negatives)
        if zeros:
            for num in P_set:
                if -1 * num in N_set:
                    res.add((-1* num, 0, num))
        if len(zeros) >= 3:
            res.add((0, 0, 0))
        
        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                target = -1 * (negatives[i] + negatives[j])
                if target in P_set:
                    res.add(tuple(sorted([negatives[i], negatives[j], target])))
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -1 * (positives[i] + positives[j])
                if target in N_set:
                    res.add(tuple(sorted([positives[i], positives[j], target])))
        return res
                
                            

s = Solution()
res = s.threeSum([-1,0,1,2,-1,-4])
print(res) 
        