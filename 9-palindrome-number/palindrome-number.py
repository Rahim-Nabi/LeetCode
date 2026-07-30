class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        r = 0
        i = x
        while i > 0:
            r = r*10 + i % 10
            i = i//10
        
        return x == r
