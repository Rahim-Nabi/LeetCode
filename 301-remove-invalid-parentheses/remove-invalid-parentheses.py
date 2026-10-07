class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()

        left_remove = 0
        right_remove = 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
                
        def dfs(i, left, right, balance, path):

            if i == len(s):
                if left == 0 and right == 0 and balance == 0:
                    res.add("".join(path))
                return
            ch = s[i]

            if ch == '(' and left > 0:
                dfs(i + 1, left - 1, right, balance, path)
            elif ch == ')' and right > 0:
                dfs(i + 1, left, right - 1, balance, path)
            

            if ch == '(':
                path.append(ch)
                dfs(i + 1, left, right, balance + 1, path)
                path.pop()
                
            elif ch == ')' and balance > 0:
                path.append(ch)
                dfs(i + 1, left, right, balance - 1, path)
                path.pop()

            elif ch != '(' and ch != ')':
                path.append(ch)
                dfs(i + 1, left, right, balance, path)
                path.pop()

        dfs(0, left_remove, right_remove, 0, [])

        return list(res)