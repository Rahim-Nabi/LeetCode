class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1
        res = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo]