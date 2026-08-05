class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lo, hi = 0, 0
        res = inf
        s = 0
        n = len(nums)
        while hi < n:
            s = s + nums[hi]
            while s >= target:
                ln = hi - lo + 1
                res = min(res, ln)
                s = s - nums[lo]
                lo += 1
            hi += 1
        if res == inf:
            return 0
        else:
            return res