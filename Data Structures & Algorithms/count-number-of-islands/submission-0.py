class Solution:

    def dfs(self, x, y, grid, visited):
        if (x, y) in visited or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0":
            return

        visited.add((x, y))

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for move in moves:
            x_new = x + move[0]
            y_new = y + move[1]

            self.dfs(x_new, y_new, grid, visited)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        x_max = len(grid)
        y_max = len(grid[0])

        count = 0

        visited = set()

        for x in range(x_max):
            for y in range(y_max):
                if grid[x][y] == "0" or (x, y) in visited:
                    continue
                
                self.dfs(x, y, grid, visited)
                count += 1

        return count