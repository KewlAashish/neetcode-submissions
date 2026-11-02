class Solution:

    def util(self, col, board, n, results, visited):
        if col == n:
            results.append(["".join(row) for row in board])
            return

        for row in range(n):
            if row in visited:
                continue

            # left diag up
            x = row - 1
            y = col - 1

            valid = True
            while x >= 0 and y >= 0:
                if board[x][y] == ".":
                    x -= 1
                    y -= 1
                else:
                    #not possible
                    valid = False
                    break

            if not valid:
                continue

            # left diag down
            x = row + 1
            y = col - 1

            while x < n and y >= 0:
                if board[x][y] == ".":
                    x += 1
                    y -= 1
                else:
                    #not possible
                    valid = False
                    break
            
            if not valid:
                continue

            visited.add(row)
            board[row][col] = "Q"
            self.util(col + 1, board, n, results, visited)
            visited.remove(row)
            board[row][col] = "."
            

    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        visited = set()
        board = [['.' for _ in range(n)] for _ in range(n)]

        self.util(0, board, n, results, visited)

        return results