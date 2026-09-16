class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = []
        freq_map = {}
        n = len(nums)
        n = n // 3
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        for num in nums:
            if freq_map[num] > n and num not in res:
                res.append(num)
            
        return res