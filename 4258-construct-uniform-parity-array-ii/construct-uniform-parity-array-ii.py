class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        c = 0
        if min(nums1) % 2 == 1:
            return True
        for i in range(n):
            if nums1[i] % 2 == 1:
                return False
        return True
