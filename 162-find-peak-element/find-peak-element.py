class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        m = n // 2
        lo, hi = 1, n - 1
        while lo <= hi:
            if nums[lo - 1] < nums[lo] > nums[lo + 1]:
                return lo
                break
            elif nums[hi - 1] < nums[hi] > nums[hi + 1]:
                return hi
                break
            lo += 1
            hi -= 1