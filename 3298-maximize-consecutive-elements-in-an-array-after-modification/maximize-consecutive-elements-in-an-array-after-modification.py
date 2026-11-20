class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp0 = {}
        dp1 = {}
        ans = 0

        for x in nums:
            old0 = dp0.get(x, 0)
            old1 = dp1.get(x, 0)

            a = 1 + max(dp0.get(x - 1, 0),
                        dp1.get(x - 2, 0))
            
            b = 1 + max(old0,
                        dp1.get(x- 1, 0))
            
            dp0[x] = max(old0, a)
            dp1[x] = max(old1, b)

            ans = max(ans, dp0[x], dp1[x])
        
        return ans