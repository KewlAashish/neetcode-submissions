
class Solution:

    def dfs(self, r, c, heights, visited):
        rows = len(heights)
        cols = len(heights[0])

        if (r, c) in visited:
            return

        visited.add((r, c))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            if (nr, nc) in visited:
                continue

            # Reverse water flow: move uphill or level
            if heights[nr][nc] >= heights[r][c]:
                self.dfs(nr, nc, heights, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        # Left and right borders
        for r in range(rows):
            self.dfs(r, 0, heights, pacific)
            self.dfs(r, cols - 1, heights, atlantic)

        # Top and bottom borders
        for c in range(cols):
            self.dfs(0, c, heights, pacific)
            self.dfs(rows - 1, c, heights, atlantic)

        result = []

        for r, c in pacific & atlantic:
            result.append([r, c])

        return result
