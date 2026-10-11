class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # Row checks:
        for row in range(9):
            temp = set()
            for i in board[row]:
                if i == ".":
                    continue
                if i in temp or i not in digits:
                    return False
                else:
                    temp.add(i)

        # Column checks:
        for col in range(9):
            temp = set()
            for i in range(9):
                val = board[i][col]
                if val == '.':
                    continue
                if val in temp or val not in digits:
                    return False
                else:
                    temp.add(val)

        # grid level checks
        col = 0
        row = 0

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                temp = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val in temp or val not in digits:
                            return False
                        temp.add(val)

        return True











