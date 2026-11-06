
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Add every treasure cell to the queue
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    queue.append((x, y))

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in moves:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                # Only visit untouched empty rooms
                if grid[nx][ny] != INF:
                    continue

                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))
