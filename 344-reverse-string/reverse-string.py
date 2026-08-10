class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        lo, hi = 0, l-1
        while lo <= hi:
            temp = s[lo]
            s[lo] = s[hi]
            s[hi] = temp
            hi -= 1
            lo += 1