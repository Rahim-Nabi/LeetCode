from collections import Counter
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        count = Counter()

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1)
                count[shift] += 1
        
        return max(count.values(), default = 0)