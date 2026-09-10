class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n1 = len(ransomNote)
        n2 = len(magazine)
        f1 = {}
        f2 = {}
        for i in range(n1):
            if ransomNote[i] in f1:
                f1[ransomNote[i]] += 1
            else:
                f1[ransomNote[i]] = 1
            
        for i in range(n2):
            if magazine[i] in f2:
                f2[magazine[i]] += 1
            else:
                f2[magazine[i]] = 1
        return self.fun(f2, f1)

    def fun(self, f2, f1):
        for ch in f1:
            if ch not in f2:
                return False
            if f1[ch] > f2[ch]:
                return False
        return True