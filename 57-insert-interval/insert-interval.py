class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        insert = False
        n = len(intervals)
        for i in range(n):
            start = intervals[i][0]
            if insert == False and start >= newInterval[0]:
                arr.append(newInterval)
                insert = True
            arr.append(intervals[i])
        if insert == False:
            arr.append(newInterval)
        res = []
        start1 = arr[0][0]
        end1 = arr[0][1]
        for i in range(1, len(arr)):
            start2 = arr[i][0]
            end2 = arr[i][1]
            if start2 <= end1:
                end1 = max(end1, end2)
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2
        res.append([start1, end1])
        return res