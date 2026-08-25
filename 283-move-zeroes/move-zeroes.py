class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lo = 0
        hi = 1
        while hi < n:
            if nums[lo] == 0 and nums[hi] != 0:
                nums[lo] = nums[hi]
                nums[hi] = 0
                lo += 1
                hi += 1
            elif nums[lo] == 0 and nums[hi] == 0:
                hi += 1
            elif nums[lo] != 0 and nums[hi] == 0:
                lo += 1
            elif nums[lo] != 0 and nums[hi] != 0:
                lo += 1
                hi += 1