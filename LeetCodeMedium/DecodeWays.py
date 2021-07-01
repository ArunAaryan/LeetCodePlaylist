#https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp
class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.helperRecursive(s, 0)
        memo = [None] * len(s)
        return self.helperMemo(s, 0, memo)
    

    def helperRecursive(self, s, current):
        if current == len(s):
            return 1
        if s[current] == "0":
            return 0
        res = self.helperRecursive(s, current + 1) 
        if current < len(s) - 1 and (s[current] == "1" or (s[current] =="2" and s[current + 1] < "7")):
            res += self.helperRecursive(s, current + 2)
        return res
#memoization with recursion
    def helperMemo(self, s, current , memo):
        if current == len(s):
            return 1
        if current == "0":
            return 0
        if memo[current]:
            return memo[current]
        res = 0
        res = self.helperMemo(s, current + 1, memo) 
        if current < len(s) - 1 and (s[current] == "1" or (s[current] == "2" and s[current + 1] < "7")):
            res += self.helperMemo(s, current + 2, memo)
        memo[current] = res
        return res 
#dp without recursion O(n) time and space

    def bottomUpn(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        if s[n-1] != 0:
            dp[n - 1] = dp[n]
        for i in range(n-2, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if (s[i] == "1" or s[i] == "2" and s[i+1]< "7"):
                    dp[i] += dp[i + 2]
        return dp[0]




s = Solution()
# res = s.numDecodings('226')
res = s.bottomUpn('226')
print(res)

 
        