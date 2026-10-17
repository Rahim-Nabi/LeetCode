class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        n = len(nums)
        sorted_nums = sorted(nums, key = lambda x: (digit_sum(x), x))

        position = {value: i for i, value in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or position[nums[i]] == i:
                continue
            
            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1
            
            swaps += cycle_size - 1
        
        return swaps