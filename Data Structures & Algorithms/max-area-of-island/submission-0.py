class Solution:
    
    def dfs(self, x, y, grid, visited):
        if (x, y) in visited or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        visited.add((x, y))
        
        count = 1

        for move in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x_new = x + move[0]
            y_new = y + move[1]

            count += self.dfs(x_new, y_new, grid, visited)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        visited = set()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) in visited or grid[x][y] == 0:
                    continue

                ans = max(ans, self.dfs(x, y, grid, visited))

        return ans