class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        z = o = 0
        f = {}
        d = res = 0
        for i in range(n):
            if nums[i] == 0:
                z += 1
            else:
                o += 1
            d = z - o
            if d == 0:
                res = max(res, i+1)
                continue
            elif d not in f:
                f[d] = i
            else:
                idx = f[d]
                l = i - idx
                res = max(l, res)

        return res