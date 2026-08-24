class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = nums[0]
        curr_max = curr_min = nums[0]
        n = len(nums)
        for i in range(1, n):
            v1 = curr_max + nums[i]
            v2 = nums[i]
            curr_max = max(v1, v2)
            max_sum = max(max_sum, curr_max)
            v1 = curr_min + nums[i]
            v2 = nums[i]
            curr_min = min(v1, v2)
            min_sum = min(curr_min, min_sum)
        min_sum = abs(min_sum)
        return max(max_sum, min_sum)