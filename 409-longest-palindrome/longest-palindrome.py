class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = {}
        for ch in s:
            f[ch] = f.get(ch, 0) + 1
        
        l = 0
        odd = False

        for count in f.values():
            l += (count // 2) * 2

            if count % 2 == 1:
                odd = True
            
        if odd:
            l += 1
        
        return l