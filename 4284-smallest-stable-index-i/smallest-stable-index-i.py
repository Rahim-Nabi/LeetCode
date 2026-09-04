class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        mx = -inf
        mn = inf
        m1 = []
        m2 = []
        while i < n  and j >= 0:
            mx = max(mx, nums[i])
            mn = min(mn, nums[j])
            m1.append(mx)
            m2.append(mn)
            i += 1
            j -= 1
        
        for i in range(n):
            if m1[i] - m2[n - 1 - i] <= k:
                return i

        return -1