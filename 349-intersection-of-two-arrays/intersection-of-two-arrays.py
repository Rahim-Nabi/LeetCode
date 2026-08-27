class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        res = set()
        for num in num1:
            if num in num2:
                res.add(num)
        return list(res)