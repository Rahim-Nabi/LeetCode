class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        one_del = -inf
        res = arr[0]
        n = len(arr)
        for i in range(1, n):
            prev_nodel = no_del
            prev_onedel = one_del
            no_del = max(prev_nodel + arr[i], arr[i])
            one_del = max(prev_nodel, prev_onedel + arr[i])
            res = max(res, max(one_del, no_del))

        return res
