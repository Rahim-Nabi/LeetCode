class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        res = []
        for i in range(n):
            c = s[i]
            if not stack:
                stack.append((c, 1))
            elif stack[-1][0] != c:
                stack.append((c, 1))
                continue
            elif stack[-1][1] < k - 1:
                p = stack[-1]
                stack.pop()
                stack.append((p[0],p[1]+1))
                continue
            else:
                stack.pop()
            
        while stack:
            p = stack[-1]
            stack.pop()
            while p[1]:
                res.append(p[0])
                p = (p[0], p[1] - 1)

        return ''.join(res[::-1])