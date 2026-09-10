class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}
        ans = -1
        n = len(s)
        for i in range(n):
            if s[i] in f:
                f[s[i]] += 1
            else:
                f[s[i]] = 1
        for i in range(n):
            if f[s[i]] == 1:
                return i
            
        return -1