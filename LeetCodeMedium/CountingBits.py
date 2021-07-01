from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
      n = num
      arr = []
      for num in range(n + 1):
          res = 0 
          while num:
              if num % 2 == 1:
                  res += 1
              num = num // 2
          arr.append(res)
      return arr
# https://leetcode.com/problems/counting-bits/discuss/79539/Three-Line-Java-Solution
    def countBitsDP(self,num):
        res =[0] * (num + 1)
        for i in range(1, num + 1):
        #  To sum up, when you meet even number the count of '1's is always the same as its half number, on the other hand, remember to plus one to the odds' half number.
            res[i] = res[i//2] + (i % 2)
            # below line is similar to above line
            # res[i] = res[i >> 1] + (i & 1)
        return res
        


s = Solution()
res = s.countBitsDP(5)
print(res)