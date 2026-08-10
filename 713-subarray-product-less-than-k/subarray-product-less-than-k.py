class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        c, p = 0, 1
        if k <= 1:
            return 0
        
        lo, hi = 0, 0
        n = len(nums)
        for hi in range (n):
            p = p * nums[hi]
            while p >= k:
                p = p // nums[lo]
                lo += 1
            c += hi - lo + 1
        return c