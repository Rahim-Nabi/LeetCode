class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = costs[i - 1] + min(
                dp[i - 1] + 1,
                dp[i -2] + 4 if i >= 2 else float('inf'),
                dp[i - 3] + 9 if i >= 3 else float('inf')
            )
        
        return dp[n]