import heapq

class Solution:
    def busiestServers(self, k, arrival, load):

        tree = [0] * (4 * k)

        # Build segment tree
        def build(node, l, r):
            if l == r:
                tree[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        # Update availability
        def update(node, l, r, pos, val):
            if l == r:
                tree[node] = val
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, val)
            else:
                update(node * 2 + 1, mid + 1, r, pos, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        # Find first available server
        def find_first(node, l, r, ql, qr):

            if ql > qr or r < ql or l > qr:
                return -1

            if tree[node] == 0:
                return -1

            if l == r:
                return l

            mid = (l + r) // 2

            ans = find_first(
                node * 2, l, mid, ql, qr
            )

            if ans != -1:
                return ans

            return find_first(
                node * 2 + 1, mid + 1, r, ql, qr
            )

        build(1, 0, k - 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:

                end_time, server = heapq.heappop(busy)

                update(1, 0, k - 1, server, 1)

            start = i % k

            # Search preferred server onwards
            server = find_first(
                1, 0, k - 1, start, k - 1
            )

            # Wrap around
            if server == -1:
                server = find_first(
                    1, 0, k - 1, 0, start - 1
                )

            # Drop request if all servers busy
            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(1, 0, k - 1, server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]