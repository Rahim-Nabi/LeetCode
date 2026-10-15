class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)

        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                    
                else:
                    flowers = 0

            return bouquets >= m
        
        while left < right:
            mid = (left + right) // 2

            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left