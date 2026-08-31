class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        for i in range(1,n):
            start2 = intervals [i][0]
            end2 = intervals [i][1]
            if start2 <= end1:
                end1 = max(end1, end2)
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2
        res.append([start1, end1])
        return res