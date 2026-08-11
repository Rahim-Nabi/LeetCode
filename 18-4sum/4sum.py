class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        lo, hi = 0, n - 1
        s1 = s2 = s = 0
        res = []
        for i in range(n -3):
            if i > 0 and nums[i] == nums [i - 1]:
                continue
            for j in range(i + 1,n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    s = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if s == target:
                        res.append([nums[i],nums[j],nums[lo],nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif s < target:
                        lo += 1
                    elif s > target:
                        hi -= 1
        return res