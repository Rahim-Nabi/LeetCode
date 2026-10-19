class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        s = []
        n = len(accounts)
        for i in range(n):
            s.append(sum(accounts[i]))
        return max(s)