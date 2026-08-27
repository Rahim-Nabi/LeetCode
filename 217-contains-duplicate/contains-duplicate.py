class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        if len(nums) != len(num):
            return True
        else:
            return False