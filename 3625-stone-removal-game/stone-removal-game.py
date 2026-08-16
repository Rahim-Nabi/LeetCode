class Solution:
    def canAliceWin(self, n: int) -> bool:
        r = 1
        d = 10
        c = 0
        while n >= d:
            n = n - d
            d -= 1
            c += 1
        return c % 2 == 1
