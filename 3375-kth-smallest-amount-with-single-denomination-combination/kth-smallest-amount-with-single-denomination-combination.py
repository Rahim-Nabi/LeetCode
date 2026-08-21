from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for c in coins:
            if all(c % x != 0 for x in new_coins):
                new_coins.append(c)

        coins = new_coins
        n = len(coins)
        def count(x):
            total = 0

            for mask in range(1,1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm // gcd(lcm, coins[i]) * coins[i]

                        if lcm > x:
                            valid = False
                            break
                        
                if not valid:
                    continue

                multiples = x // lcm
                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples
                
            return total
        
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left