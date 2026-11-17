class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = float('inf')

        # Step 1: Precompute substring costs
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):

                best = INF

                # Try every proper divisor
                for d in range(1, length):

                    if length % d != 0:
                        continue

                    changes = 0
                    group_size = length // d

                    # Check each group
                    for offset in range(d):

                        for t in range(group_size // 2):

                            left = l + offset + t * d
                            right = l + offset + (group_size - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    best = min(best, changes)

                cost[l][l + length - 1] = best

        # Step 2: Dynamic Programming
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for g in range(1, k + 1):

            for i in range(2 * g, n + 1):

                for j in range(2 * (g - 1), i - 1):

                    dp[g][i] = min(
                        dp[g][i],
                        dp[g - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]