class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lo = 0
        hi = 0
        n = len(s)
        for ch in s:
            if ch == '(':
                lo += 1
            else:
                if lo > 0:
                    lo -= 1
                else:
                    hi += 1
        
        return hi + lo