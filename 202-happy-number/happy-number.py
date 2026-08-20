class Solution:
    def digsq(self, n: int):
        s = 0
        while n > 0:
            d = n % 10
            s = s + (d * d)
            n = n // 10
        return s
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while fast != 1:
            slow = self.digsq(slow)
            fast = self.digsq(fast)
            fast = self.digsq(fast)
            if slow == fast and slow != 1:
                return False
            
        return True
        