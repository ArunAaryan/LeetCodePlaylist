from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1: #if there is only one option that is to buy then there is no profit
            return 0
        rest = [0] * l # to wait after selling or to wait after buying  
        buy = [0] * l # to wait or just buy  
        sell = [0] * l # to sell 
        buy[0] = -prices[0] #first stock definitely needs to bought as initial start
        sell[0] = -float('inf') #profit left after selling
        for today in range(1, l): #as the base case is written for first day. we start from second day
            rest[today] = max(rest[today - 1], sell[today - 1]) # max profit by not buying or resting after selling previous day. 
            buy[today] = max(buy[today - 1], rest[today - 1] - prices[today]) # max profit after buying or resting simply
            sell[today] = buy[today - 1] + prices[today] # what profit do we get if we sell the stock today.
        print(rest) 
        print(buy) 
        print(sell) 
        return max(rest[l - 1], sell[l - 1]) #if we can no more sell stock return the previous profit else current profit after selling.
s = Solution()
res = s.maxProfit([1,2,3,5,10,20])
print(res)
