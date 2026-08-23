class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        s1, q1 = 0, 0
        s2, q2 = 0, 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    q1 += 1
                else:
                    s1 += int(num[i])
                
            else:
                if num[i] == '?':
                    q2 += 1
                else:
                    s2 += int(num[i])
                
        return (q1 + q2) % 2 == 1 or s1 - s2 != (q2 - q1) // 2 * 9