class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        time = 0
        count_fresh_fruits = 0

        # returning minus 1 when after the complete bfs we still have good oranges
        bfs = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    bfs.append((x, y))
                if grid[x][y] == 1:
                    count_fresh_fruits += 1
        
        if count_fresh_fruits == 0:
            return time
        
        while bfs:
            n = len(bfs)
            time += 1

            for i in range(n):
                x, y = bfs.popleft()

                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue

                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        count_fresh_fruits -= 1
                        bfs.append((nx, ny))

        if count_fresh_fruits:
            return -1

        return time - 1