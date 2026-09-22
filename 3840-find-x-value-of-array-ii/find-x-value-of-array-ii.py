class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def make_node(value):
            rem = value % k

            cnt = [0] * k 
            cnt[rem] = 1
            return [rem, cnt]
        
        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            cnt = left_cnt[:]

            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]
            prod = (left_prod * right_prod) % k
            return [prod, cnt]
        
        def build(node, l , r):
            if l == r:
                tree[node] = make_node(nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        
        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = make_node(value)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)
            
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            
            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)
        
        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            res = query(1, 0, n-1, start, n - 1)

            ans.append(res[1][x])

        return ans