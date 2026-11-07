import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []

        ans = []

        current_time = 0

        for i, duration in enumerate(tasks):

            current_time = max(current_time, i)

            # Release all servers that are free
            while busy and busy[0][0] <= current_time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, advance time
            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    _, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Mark the server as busy
            heapq.heappush(
                busy,
                (current_time + duration, weight, idx)
            )

        return ans