class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (stack[-1] == "(" and s[i] == ")") or \
                (stack[-1] == "{" and s[i] == "}") or \
                (stack[-1] == "[" and s[i] == "]"):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True