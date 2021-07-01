from typing import List
class Solution:
    def productExceptSelfNaive(self, nums: List[int]) -> List[int]:
        zero = 0
        res = 1
        new_arr = [0] * len(nums)
        for idx, val in enumerate(nums):
            if val == 0:
                zero += 1
            else:
                res *= val
        
        for idx, val in enumerate(nums):
           if val == 0:
                new_arr[idx] = res
           elif zero:
                new_arr[idx] = 0
           else:
                new_arr[idx]  = res // val

        if zero == len(nums) or zero >=2:
            return [0] * len(nums)
        return new_arr
       
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res1 = [1] * len(nums)
        res1[0] = 1
        prod = 1
        for i in range(1, len(nums)):
            res1[i] = prod * nums[i-1]
            prod *= nums[i-1]
        print(res1)
        prod = 1
        for j in range(len(nums) -2 , -1, -1):
            res1[j] = res1[j] * nums[j+1] * prod
            prod *= nums[j+1]
            # print(j)
        # return res1    

    def editorsSolution(self, nums):
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all 
        # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        print(answer)
        R = 1;
        for i in reversed(range(length)):
            print(i)

        # For the index 'i', R would contain the 
        # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        # return answer

    #Best and concise solution
    def productExceptSelfBest(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
    
# s = Solution()
# # print(s.([2,3,5,0]))
# print(s.productExceptSelf([2,3,5,0]))
# print(s.editorsSolution([2,3,5,0]))