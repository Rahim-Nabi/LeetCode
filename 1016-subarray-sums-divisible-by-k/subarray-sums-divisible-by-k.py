class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        s = 0
        f = {}
        f[0] = 1
        for i in range(n):
            s += nums[i]
            rem = s % k
            if rem < 0:
                rem += k
            res += f.get(rem, 0)
            f[rem] =  f.get(rem, 0) + 1
        return res