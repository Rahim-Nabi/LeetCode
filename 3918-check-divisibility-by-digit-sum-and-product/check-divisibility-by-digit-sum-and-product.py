class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        c = n
        while n > 0:
            r = n % 10
            s = s + r
            p = p * r
            n = n // 10

        s = s + p
        if c % s == 0:
            return True
        else:
            return False