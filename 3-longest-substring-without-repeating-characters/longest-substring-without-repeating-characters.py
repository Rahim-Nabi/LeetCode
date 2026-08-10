class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        longest = -inf
        hi = 0
        sett = set()
        n = len(s)
        if n == 0:
            return 0

        for hi in range(n):
            while s[hi] in sett:
                sett.remove(s[lo])
                lo += 1
            w = hi - lo + 1
            longest = max(longest, w)
            sett.add(s[hi])

        return longest
