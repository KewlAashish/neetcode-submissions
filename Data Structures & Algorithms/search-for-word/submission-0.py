class Solution:

    def is_valid(self, x, y, x_max, y_max):
        if x >= 0 and x < x_max and y >= 0 and y < y_max:
            return True

        return False

    def util(self, x, y, word_ind, board, word, visited):
        if word_ind == len(word):
            return True

        if not self.is_valid(x, y, len(board), len(board[0])):
            return False

        if visited[x][y]:
            return False

        outcome = False
        

        if board[x][y] != word[word_ind]:
            return False
        else:
            visited[x][y] = True
            for moves in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                outcome = outcome | self.util(x + moves[0], y + moves[1], word_ind + 1, board, word, visited)
            visited[x][y] = False

        return outcome


    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        x_max, y_max = len(board), len(board[0])

        for x in range(x_max):
            for y in range(y_max):
                # Check if this matches the starting character of the word
                if board[x][y] == word[0]:
                    visited = [[False] * y_max for _ in range(x_max)]
                    # visited[x][y] = True

                    if self.util(x, y, 0, board, word, visited):
                        return True

        return False