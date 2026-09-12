from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            (e, s, w, i)
            for i, (s, e, w) in enumerate(intervals)
        )

        ends = [x[0] for x in arr]

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):

                best = dp[k][i - 1]

                end, start, weight, idx = arr[i - 1]

                p = bisect_left(ends, start, 0, i - 1)

                prev_score, prev_indices = dp[k - 1][p]

                candidate = (
                    prev_score + weight,
                    tuple(sorted(prev_indices + (idx,)))
                )

                if (candidate[0] > best[0] or
                    (candidate[0] == best[0] and
                    candidate[1] < best[1])):
                    best = candidate

                dp[k][i] = best

        return list(min(
            [dp[k][n] for k in range(1, 5)],
            key=lambda x: (-x[0], x[1])
        )[1])