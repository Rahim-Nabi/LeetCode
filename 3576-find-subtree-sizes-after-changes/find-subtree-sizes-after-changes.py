class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # New parent array
        new_parent = [-1] * n

        # Track the nearest ancestor for each character
        last = {}

        # Iterative DFS on original tree
        stack = [(0, False, None)]

        while stack:
            node, exiting, prev = stack.pop()

            if exiting:
                # Restore previous character mapping
                if prev is None:
                    last.pop(s[node], None)
                else:
                    last[s[node]] = prev
                continue

            char = s[node]

            # Find nearest ancestor with same character
            if node != 0:
                new_parent[node] = last.get(char, parent[node])

            # Save previous mapping
            prev = last.get(char)

            # Current node becomes the latest occurrence
            last[char] = node

            # Backtracking event
            stack.append((node, True, prev))

            # Visit original children
            for child in children[node]:
                stack.append((child, False, None))

        # Build modified tree
        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        # Postorder traversal
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Calculate subtree sizes
        answer = [1] * n

        for node in reversed(order):
            for child in new_children[node]:
                answer[node] += answer[child]

        return answer