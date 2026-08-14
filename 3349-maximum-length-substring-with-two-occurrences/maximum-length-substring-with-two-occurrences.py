class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        lo = 0
        hi = 0
        longest = -inf
        c = {}
        n = len(s)
        if n == 0:
            return 0
        for hi in range(n):
            c[s[hi]] = c.get(s[hi], 0) + 1
            while c[s[hi]] > 2:
                c[s[lo]] -= 1
                lo += 1
            longest = max(longest, hi - lo + 1)
        
        return longest