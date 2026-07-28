class Solution:
    from typing import List
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        c=0
        for num in nums:
            c += num
            running_sum.append(c)
        
        return running_sum