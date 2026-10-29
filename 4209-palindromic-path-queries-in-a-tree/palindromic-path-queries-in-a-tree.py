class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        order = []

        stack = [0]
        parent[0] = 0

        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)

            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        
        size = [1] * n
        tout = [0] * n

        for u in reversed(order):
            if u != 0:
                size[parent[u]] += size[u]
        
        for u in range(n):
            tout[u] = tin[u] + size[u] - 1
        
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            
            if u == v:
                return u
            
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
                
            return parent[u]

        bit = [0] * (n + 1)
        def add(i, val):
            while i <= n:
                bit[i] ^= val
                i += i & -i
            
        def prefix(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result
        
        chars = list(s)
        base = [0] * n
        for u in order:
            mask = 1 << (ord(chars[u]) - ord('a'))
            if u == 0:
                base[u] = mask
            else:
                base[u] = base[parent[u]] ^ mask
        
        def path_mask(u):
            return base[u] ^ prefix(tin[u] + 1)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                chars[u] = c

                add(tin[u] + 1, delta)
                add(tout[u] + 2, delta)
            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                mask = (
                    path_mask(u)
                    ^ path_mask(v)
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                ans.append((mask & (mask - 1)) == 0)
        return ans