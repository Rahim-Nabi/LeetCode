class Solution:
    def minInsertions(self, s: str) -> int:
        insertion = 0
        need = 0
        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    insertion += 1
                    need -= 1
                
                need += 2
            
            else:
                need -= 1

                if need < 0:
                    insertion += 1
                    need = 1
                
        return insertion + need