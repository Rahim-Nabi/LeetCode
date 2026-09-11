class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1
        
        count = 0
        n = len(digits)

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):
                    if freq[a] == 0:
                        continue
                    
                    if freq[b] == 0:
                        continue
                    
                    if freq[c] == 0:
                        continue

                    if a == b == c:
                        if freq[a] < 3:
                            continue
                    elif a == b:
                        if freq[a] < 2:
                            continue
                    elif a == c:
                        if freq[a] < 2:
                            continue
                    
                    elif b == c:
                        if freq[b] < 2:
                            continue
                    count += 1
        return count