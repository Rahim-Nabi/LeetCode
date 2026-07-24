class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while j>i:
            if numbers[i] + numbers[j] < target:
                i=i+1
            elif numbers[i] + numbers[j] > target:
                j=j-1
            else:
                return i+1,j+1