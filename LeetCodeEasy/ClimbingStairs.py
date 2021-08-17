#Day 2


def climbStairsNaive(step, n): # O2n solution
    if step > n:
        return 0
    if step == n:
        return 1
    return climbStairsNaive(step+1,n) + climbStairsNaive(step+2, n)
#dynamic programming
# With memoization parallel recursion depths are avoided and stack recomputation is avoided.
def climbStairsMemo(step, n, memo):
    if step > n:
        return 0
    if step == n:
        return 1
    if memo[step] > 0:
        return memo[step]

    memo[step] = climbStairsMemo(step+1,n, memo) + climbStairsMemo(step+2, n, memo)
    return memo[step]

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
    for step in range(3, n+1):
        dp[step] = dp[step-1] + dp[step-2]
    return dp[n]

# print(climbStairsdp(4))




