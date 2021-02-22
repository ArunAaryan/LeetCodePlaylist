from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i+1):
                if s[j: i+1] in wordDict and (j== 0 or dp[j-1]):
                    dp[i] = True
                    break
        return dp[len(s)-1]


s = Solution()
print(s.wordBreak('catsandogs',["cats","and","dogs"]))