class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        arr = list(enumerate(nums))
        def merge_sort(left, right):
            if right - left <= 1:
                return
            
            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)
            temp = []
            i = left
            j = mid
            smaller = 0

            while i < mid and j < right:
                if arr[j][1] < arr[i][1]:
                    temp.append(arr[j])
                    smaller += 1
                    j += 1
                
                else:
                    counts[arr[i][0]] += smaller
                    temp.append(arr[i])
                    i += 1
            
            while i < mid:
                counts[arr[i][0]] += smaller
                temp.append(arr[i])
                i += 1
            
            while j < right:
                temp.append(arr[j])
                j += 1
            arr[left:right] = temp
        
        merge_sort(0, n)
        return counts