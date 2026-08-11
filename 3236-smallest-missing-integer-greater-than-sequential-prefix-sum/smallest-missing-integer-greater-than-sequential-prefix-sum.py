class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        for j in range (1, n):
            if nums[j] == nums[j - 1] + 1:
                s = s + nums[j]
            else:
                break
        while s in nums:
            s += 1
            
        return s