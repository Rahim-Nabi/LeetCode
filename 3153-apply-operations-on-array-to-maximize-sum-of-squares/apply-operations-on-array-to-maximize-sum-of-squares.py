class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 32
        for num in nums:
            for bit in range(32):
                if (num >> bit) & 1:
                    cnt[bit] += 1
            
        ans = 0

        for _ in range(k):
            num = 0
            for bit in range(32):
                if cnt[bit] > 0:
                    num |= (1 << bit)
                    cnt[bit] -= 1
                
            ans = (ans + num * num) % MOD

        return ans