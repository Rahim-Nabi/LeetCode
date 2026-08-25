class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        n = len(nums)
        left = 0
        for i in range (n):
            right = summ - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1