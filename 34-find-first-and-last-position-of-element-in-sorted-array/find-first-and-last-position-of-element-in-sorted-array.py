class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        n = len(nums)
        hi = n - 1
        f = -1
        l = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                f = mid
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        lo = 0
        hi = n - 1
        l = - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                l = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
            
        return [f, l]