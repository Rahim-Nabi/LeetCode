class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for (r, c) in reservedSeats:
            d[r] |= 1 << (c - 1)

        ans = 2 * n
        for r, binary in d.items():
            if binary | 513 == 513:
                continue
            elif binary | 543 == 543 or binary | 903 == 903 or binary | 993 == 993:
                ans -= 1
            else:
                ans -= 2
            
        return ans