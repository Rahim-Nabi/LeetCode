class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]
        start = 0

        for end in range(1, n + 1):

            if end == n or arr[end][0] - arr[end - 1][0] > limit:

                group = arr[start:end]

                indices = sorted(i for _, i in group)
                
                for (value, _), index in zip(group, indices):
                    ans[index] = value
                
                start = end
            
        return ans