class Solution:
    def fun(self, a: list[int], n: int, speed: int) -> int:
        h = 0
        for i in range(n):
            h = h + a[i] // speed
            if(a[i] % speed != 0):
                h += 1

        return h
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        lo = 1
        hi = max(piles)
        res = hi
        while lo <= hi:
            guess = (lo + hi) // 2
            hour = self.fun(piles, n, guess)
            if(hour > h):
                lo = guess + 1
            else:
                res = guess
                hi = guess - 1
        
        return res