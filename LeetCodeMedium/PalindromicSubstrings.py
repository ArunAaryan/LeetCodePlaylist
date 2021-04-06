class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for low in range(n):
            for high in range(low, n):
                ans += self.isPalindrome(low, high, s)
        return ans

    def isPalindrome(self, low, high, s):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
    def countSubStringsdp(self, s):
        n = len(s)
        if n == 0:
            return 0 
        count = 0
        dp = [[False] * n for _ in range(n)]

        # base case : every char is a palindrome of length 1
        for i in range(n):
            dp[i][i] = True
            count += 1

        # base case : two adjacent chars can be palindrome of length 2
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        for subStringLen in range(3, n + 1):
            left = 0
            right = left + subStringLen - 1
            while (right < n):
                dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                count += dp[left][right]
                left += 1
                right += 1
        return count
    def countSubStringsExpand(self, s):
        count = 0
        n = len(s)
        for i in range(n):
            count += self.expandAroundCenter(s, i, i)

            count += self.expandAroundCenter(s, i, i + 1)
        
        return count
    
    def expandAroundCenter(self, s, low, high):
        count = 0
        while low >= 0 and high < len(s):
            if s[low] != s[high]:
                break
            low -= 1
            high += 1
            count += 1
        return count


            
s = Solution()
# s.isPalindrome(0,2,"aba")
res = s.countSubStringsExpand("saaas")
print(res)