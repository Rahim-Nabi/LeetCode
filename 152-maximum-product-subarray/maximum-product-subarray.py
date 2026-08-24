class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_end = max_end = res = nums[0]
        n = len(nums)
        for i in range(1, n):
            v1 = nums[i]
            v2 = min_end * nums[i]
            v3 = max_end * nums[i]
            max_end = max(v1, max(v2, v3))
            min_end = min(v1, min(v2, v3))
            res = max(res, max(min_end, max_end))

        return res