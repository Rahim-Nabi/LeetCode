class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = n - 1
        s = 0
        dig = []
        for i in range(n):
            s = s * 10 + digits[i]
            c -= 1
        s = s + 1
        while s > 0:
            d = s % 10
            s = s // 10
            dig.append(d)

        return (dig[::-1])