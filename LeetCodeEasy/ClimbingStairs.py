#Day 2


def climbStairsNaive(i, n): # O2n solution
    if i > n:
        return 0
    if i == n:
        return 1
    return climbStairsNaive(i+1,n) + climbStairsNaive(i+2, n)
#dynamic programming
# With memoization parallel recursion depths are avoided and stack recomputation is avoided.
def climbStairsMemo(i, n, memo):
    if i > n:
        return 0
    if i == n:
        return 1
    if memo[i] > 0:
        return memo[i]

    memo[i] = climbStairsMemo(i+1,n, memo) + climbStairsMemo(i+2, n, memo)
    return memo[i]

# print(climbStairsMemo(0, 3,[0]*4))

#approach 3 is dynamic programming 
#dividing the problem into multiple subproblems so instead of thinking of n we think of  1,2,3,4,5....n
# dp 0 1 2 3 5 8 13
#    0 1 2 3 4 5 8

#iterative dp step

def climbStairsdp(n):
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# print(climbStairsdp(4))




