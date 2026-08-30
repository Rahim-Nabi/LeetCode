class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 2
        l1 = l2 = s1 = s2 = 0
        r = 0
        largest = -inf
        smallest = inf
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]
                l = i 
            if nums[i] < smallest:
                smallest = nums[i]
                s = i
        front = max(l, s) + 1
        back = n - min(l, s)
        both = min(l, s) + 1 + n -max(l , s)

        return min(front, back, both)