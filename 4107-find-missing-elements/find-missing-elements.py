class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        mn, mx = inf, -inf
        for n in nums:
            mn = min(mn, n)
            mx = max(mx,n)
        res = []
        for n in range(mn, mx + 1):
            if not n in nums:
                res.append(n)
        
        return res
