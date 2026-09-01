from collections import deque
from typing import List
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = [[-1] * n for _ in range(m)]

        start = 0
        k = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = r * n + c
                
                elif classroom[r][c] == 'L':
                    litter[r][c] = k
                    k += 1

        if k == 0:
            return 0
        
        full = (1 << k) - 1

        q = deque([(start, energy, full)])
        best = {(start, full): energy}

        moves = 0

        while q:
            for _ in range(len(q)):
                pos, e, mask = q.popleft()

                if mask == 0:
                    return moves

                if e == 0:
                    continue
                
                r, c = divmod(pos, n)

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nm = mask

                    cell = classroom[nr][nc]

                    if cell == 'R':
                        ne = energy
                    elif cell == "L":
                        nm &= ~(1 << litter[nr][nc])

                    np = nr * n + nc

                    key = (np, nm)

                    if ne <= best.get(key, -1):
                        continue
                    
                    best[key] = ne
                    q.append((np, ne, nm))
            moves += 1
        return -1