class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Intuition is clear for these kind of problems to start from the last stage.
        Basically a multisource BFS using the r, c = "O" on the borders

        Start iterating from them and traverse to connected "O" cells.
        And maybe mark them as -1, add them to queue

        Then once the whole thing is done with, replace remaining "O" with "X"
        and the -1 with "O"
        """

        rows = len(board)
        cols = len(board[0])

        visited = set()

        bfs = deque()

        # Top, Bottom, Left and right border
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O" and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1):
                    visited.add((x, y))
                    bfs.append((x, y))
                    board[x][y] = "T"

        while bfs:
            x, y = bfs.popleft()

            board[x][y] = "T"

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx > rows - 1 or ny < 0 or ny > cols - 1:
                    continue

                if (nx, ny) in visited:
                    continue
                
                if board[nx][ny] == "O":
                    visited.add((nx, ny))
                    bfs.append((nx, ny))

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "T":
                    board[x][y] = "O"

        return

