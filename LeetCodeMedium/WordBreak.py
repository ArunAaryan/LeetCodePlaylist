from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
    def wordBreakBruteForce(self, s, wordDict):
        dictSet = set({})
        return self.wordBreakHelper(s, dictSet)
    def wordBreakHelper(self, s, dictSet):
        slen = len(s) 
        if slen == 0 :
            return True
        for i in range(1, slen + 1):
            if s[0:1] in dictSet and self.wordBreakHelper(s[i], dictSet):
                return True
        return



s = Solution()
print(s.wordBreak('catsandogs',["catsand","cats","dogs"]))