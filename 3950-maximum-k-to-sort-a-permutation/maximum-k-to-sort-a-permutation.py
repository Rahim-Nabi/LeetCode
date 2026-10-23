class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == list(range(n)):
            return 0
        
        ans = (1 << 31) - 1

        for i, num in enumerate(nums):
            if i != num:
                ans &= num
            
        return ans