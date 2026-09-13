class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        lo = 0
        hi = n - 1
        res = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                res = mid
                hi = mid - 1

        return res
