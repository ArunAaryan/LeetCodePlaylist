#https://leetcode.com/problems/unique-paths/discuss/22953/Java-DP-solution-with-complexity-O(n*m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #unique paths using 2-D array
        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]
    
    def printdp(self, dp):
        for i in (dp):
            print(i)
        


s = Solution()
res = s.uniquePaths(3,2)
print(res)
        