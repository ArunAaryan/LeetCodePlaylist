class Solution:
    def lengthOfLongestSubstring(self, s):
        start = res = maximum = 0
        count={}
        for end in range(len(s)):
            val = count.get(s[end],0)
            if val:
                while s[start] != s[end]:
                    start += 1
                    count.pop(s[start])
                start += 1
                if count.get(s[start], 0):
                    count.pop(s[start])
            else:
                count[s[end]] = 1
                maximum = max(maximum, end- start + 1)

            res = max(maximum, res) 
        return res

s = Solution()
res = s.lengthOfLongestSubstring("tm mzux t")
print(res)
            
        