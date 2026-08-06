class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        n = x
        if n < 0:
            sign = -1
            n = n * -1
        while n > 0:
            d = n % 10
            rev = rev * 10 + d
            n = n // 10
        if not -2**31 <rev < 2**31:
            return 0
        return rev * sign