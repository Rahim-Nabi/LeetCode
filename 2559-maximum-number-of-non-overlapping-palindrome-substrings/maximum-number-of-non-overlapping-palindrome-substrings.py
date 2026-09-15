class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [False] * n

        dp = [0] * (n + 1)

        for i in range(n):
            for j in range(i + 1):
                pal[j] = (
                    s[j] == s[i]
                    and (i - j <= 2 or pal[j + 1])
                )

                if pal[j]:
                    length = i - j +1
                    if length >= k:
                        dp[i + 1] = max(
                            dp[i + 1],
                            dp[j] + 1
                        )
            
            dp[i + 1] = max(dp[i + 1], dp[i])
        
        return dp[n]