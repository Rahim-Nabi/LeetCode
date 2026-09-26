class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = dict(knowledge)
        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = []
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                
                key = ''.join(key)

                ans.append(mp.get(key, '?'))
                i += 1
            
            else:
                ans.append(s[i])
                i += 1
            
        return ''.join(ans)