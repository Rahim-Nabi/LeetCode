class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        pivot = -1
        greater_char = -1
        for i in range(n):
            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if freq[c] > 0:
                    pivot = i
                    greater_char = c
                    break
                
            if freq[t] == 0:
                break

            freq[t] -= 1

        if pivot == -1:
            return ""
            
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
            
        ans = list(target[:pivot])

        for ch in target[:pivot]:
            freq[ord(ch) - ord('a')] -= 1

        ans.append(chr(greater_char + ord('a')))
        freq[greater_char] -= 1

        for c in range(26):
            ans.extend([chr(c + ord('a'))] * freq[c])

        return ''.join(ans)