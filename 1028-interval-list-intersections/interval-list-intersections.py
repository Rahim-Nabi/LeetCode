class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(firstList)
        m = len(secondList)
        i = j = 0
        while i < n and j < m:
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            if start1 <= start2:
                if end1 >= start2:
                    start = max(start1, start2)
                    end = min(end1, end2)
                    res.append([start, end])
            else:
                if end2 >= start1:
                    start = max(start1, start2)
                    end = min(end1, end2)
                    res.append([start, end])
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return res