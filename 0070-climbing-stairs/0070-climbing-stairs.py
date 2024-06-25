class Solution:
    # Method I -> Recursion + memoization
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 1 or n == 0:
            return 1
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]

    # Method II -> Bottom up
    # def climbStairs(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return 1
        
    #     dp = [0] * (n + 1)
    #     dp[0] = dp[1] = 1
    #     for i in range(2, n+1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
        
    #     return dp[n]