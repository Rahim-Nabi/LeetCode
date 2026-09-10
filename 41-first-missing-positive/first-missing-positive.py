class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums.sort()
        n = len(nums)
        for i in range(n):
            if res == nums[i]:
                res += 1
        
        return res