class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        num = set(nums)
        c = 0
        while c in num:
            c += 1
        return c