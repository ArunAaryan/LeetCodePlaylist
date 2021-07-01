from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [ float('inf') for _ in range(amount)]
        for amountNow in range(1, amount+1):
            for coin in coins:
                if amountNow - coin >= 0:
                    dp[amountNow] = min(dp[amountNow], dp[amountNow - coin]+1)
        
        if dp[-1] == float('inf'): return -1
        return dp[-1]



s = Solution()
res = s.coinChange([1,2,5],10)
print(res)
        