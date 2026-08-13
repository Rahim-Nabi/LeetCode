class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        lo = 0
        c = [0] * 26
        for r in range(len(s)):
            c[ord(s[r]) - 65] += 1
            while (r - lo + 1) - max(c) > k:
                c[ord(s[lo]) - 65] -= 1
                lo += 1

            longest = max(longest, (r - lo + 1))

        return longest