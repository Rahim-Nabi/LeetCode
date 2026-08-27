class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        f = {}
        f[0] = 1
        res = 0
        n = len(nums)
        for i in range(n):
            s += nums[i]
            q = s - k
            freq = f.get(q, 0)
            res += freq
            f[s] = f.get(s, 0) + 1
        return res