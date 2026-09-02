class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map [num] += 1
            else:
                freq_map [num] = 1
        for num in nums:
            if freq_map [num] == 1:
                return num