class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        total = sum(stones)
        
        best = total

        prefix_sum = total

        for i in range(len(stones) - 2, 0, -1):
            prefix_sum -= stones[i + 1]

            best = max(best, prefix_sum - best)
        
        return best