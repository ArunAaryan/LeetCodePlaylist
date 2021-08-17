#day 3
#Approach 1
import sys
def maxProfit(prices):
    max_profit = 0
    min_price = sys.maxsize
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit: 
            max_profit = price - min_price
    return max_profit

#Approach sliding window 
def maxProfitSlidingWindow(prices):
    buy, sell = 0, 1
    max_profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        sell += 1
    return max_profit

print(maxProfitSlidingWindow([7,6,2,1,8]))
