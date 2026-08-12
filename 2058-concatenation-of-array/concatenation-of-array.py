class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range (n):
            ans.append(nums[i])
        for i in range (n):
            ans.append(nums[i])
        return ans