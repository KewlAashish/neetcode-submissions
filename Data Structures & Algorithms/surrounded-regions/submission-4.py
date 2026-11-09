
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        bfs = deque()

        # Collect border O cells
        for x in range(rows):
            for y in range(cols):
                if (
                    board[x][y] == "O"
                    and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1)
                ):
                    board[x][y] = "T"
                    bfs.append((x, y))

        # BFS from all border-connected O cells
        while bfs:
            x, y = bfs.popleft()

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                if board[nx][ny] == "O":
                    board[nx][ny] = "T"
                    bfs.append((nx, ny))

        # Convert surrounded O to X and restore safe O
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "T":
                    board[x][y] = "O"
