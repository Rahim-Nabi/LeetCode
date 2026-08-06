class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = 1
            cp = n
            while cp > 0:
                d = cp % 10
                p = p * d
                cp = cp // 10
            if p % t == 0:
                return n
            n += 1