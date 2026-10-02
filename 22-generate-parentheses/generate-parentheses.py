class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(cur, open_count, close_count):
            if len(cur) == 2 * n:
                result.append(cur)

                return
            
            if open_count < n:
                backtrack(cur + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result