class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        if sum(x % 2 for x in cnt) > 1:
            return ""

        half_cnt = [x // 2 for x in cnt]

        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                middle = chr(i + 97)
                break

        rem = half_cnt[:]
        k = 0
        
        while k < half:
            x = ord(target[k]) - 97

            if rem[x] == 0:
                break
            
            rem[x] -= 1
            k += 1

        if k == half:

            left = target[:half]

            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate
            
            rem = half_cnt[:]

            for i in range(half):
                rem[ord(target[i]) - 97] -= 1

            for i in range(half - 1, -1, -1):
                x = ord(target[i]) - 97

                rem[x] += 1

                for c in range(x + 1, 26):

                    if rem[c] == 0:
                        continue

                    rem[c] -= 1

                    left = target[:i] + chr(c + 97)

                    for j in range(26):
                        left += chr(j + 97) *rem[j]

                    return left + middle + left[::-1]
                
            return ""

        for i in range(k, -1, -1):

            x = ord(target[i]) - 97

            if i < k:
                rem[x] += 1

            for c in range(x + 1, 26):

                if rem[c] == 0:
                    continue
                
                rem[c] -= 1

                left = target[:i] + chr(c + 97)
                for j in range(26):
                    left += chr(j + 97) * rem[j]

                return left + middle + left[::-1]
            
        return ""