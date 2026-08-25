class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        curr = k
        while curr in nums:
            curr = curr + k
        return curr