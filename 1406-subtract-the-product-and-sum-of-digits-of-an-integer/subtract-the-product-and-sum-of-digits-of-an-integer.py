class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p =0, 1
        i = n
        while i > 0:
            d = i % 10
            s = s + d
            p = p * d
            i = i//10
        r = p - s
        return r