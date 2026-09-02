class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        stack = []
        res = []
        for i in range(n):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        while stack:
            res.append(stack[-1])
            stack.pop()

        return ''.join(res[::-1])