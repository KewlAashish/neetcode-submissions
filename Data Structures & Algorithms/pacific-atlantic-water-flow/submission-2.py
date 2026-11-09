class Solution:

    def bfs(self, queue, heights, visited):
        rows = len(heights)
        cols = len(heights[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if (nr, nc) in visited:
                    continue

                # Reverse water flow
                if heights[nr][nc] < heights[r][c]:
                    continue

                visited.add((nr, nc))
                queue.append((nr, nc))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        # Initialize all ocean-border cells
        for r in range(rows):
            pacific.add((r, 0))
            pacific_queue.append((r, 0))

            atlantic.add((r, cols - 1))
            atlantic_queue.append((r, cols - 1))

        for c in range(cols):
            if (0, c) not in pacific:
                pacific.add((0, c))
                pacific_queue.append((0, c))

            if (rows - 1, c) not in atlantic:
                atlantic.add((rows - 1, c))
                atlantic_queue.append((rows - 1, c))

        self.bfs(pacific_queue, heights, pacific)
        self.bfs(atlantic_queue, heights, atlantic)

        return [[r, c] for r, c in pacific & atlantic]
