class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_map = {}
        res = []
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        sorted_nums = sorted(freq_map, key = freq_map.get, reverse = True)

        for i in range(k):
            res.append(sorted_nums[i])
        return res