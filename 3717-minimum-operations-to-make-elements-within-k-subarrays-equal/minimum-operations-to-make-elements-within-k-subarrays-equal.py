class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        size = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick trees
        countBIT = [0] * (size + 1)
        sumBIT = [0] * (size + 1)

        def update(bit, i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        # Find the index of the kth smallest element
        def kth(kth):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= size and countBIT[nxt] < kth:
                    idx = nxt
                    kth -= countBIT[nxt]

                step >>= 1

            return idx + 1

        # Calculate the minimum cost of every window
        costs = []
        window_sum = 0

        for i in range(n):
            v = nums[i]
            r = rank[v]

            update(countBIT, r, 1)
            update(sumBIT, r, v)
            window_sum += v

            # Remove outgoing element
            if i >= x:
                old = nums[i - x]
                old_r = rank[old]

                update(countBIT, old_r, -1)
                update(sumBIT, old_r, -old)
                window_sum -= old

            if i >= x - 1:
                # Lower median
                median_idx = kth((x + 1) // 2)
                median = vals[median_idx - 1]

                left_count = query(countBIT, median_idx)
                left_sum = query(sumBIT, median_idx)

                right_count = x - left_count
                right_sum = window_sum - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # Dynamic Programming
        INF = float('inf')

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for i in range(n + 1):
            for t in range(k + 1):

                if dp[t][i] == INF:
                    continue

                current = dp[t][i]

                # Choice 1: Skip current position
                if i < n:
                    dp[t][i + 1] = min(
                        dp[t][i + 1],
                        current
                    )

                # Choice 2: Select a window of size x
                if t < k and i + x <= n:
                    dp[t + 1][i + x] = min(
                        dp[t + 1][i + x],
                        current + costs[i]
                    )

        return dp[k][n]