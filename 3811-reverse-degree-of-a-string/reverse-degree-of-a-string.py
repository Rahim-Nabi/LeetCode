class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(c) - 97)) * i
                    for i, c in enumerate(s, 1))