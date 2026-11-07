from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]],
                     x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(enumerate(queries),
                                key=lambda q: q[1])

        count = {}
        active = 0
        left = 0
        right = 0
        ans = [0] * len(queries)

        for idx, q in sorted_queries:

            # Add logs up to current query time
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count.get(server, 0) == 0:
                    active += 1

                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs outside the window
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans