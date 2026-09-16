class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        nums.sort()
        n = len(nums)
        m = n // 2
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        for num in nums:
            if freq_map[num] > m:
                return num
    