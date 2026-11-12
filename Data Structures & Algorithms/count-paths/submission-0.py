class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        possible moves: row + 1 or col + 1
        R,R,R,R,R,D,D

        """

        dp = {}

        def is_valid(x, y):
            if x < m and y < n:
                return True

            return False

        def util(x, y):
            if not is_valid(x, y):
                return 0

            if x == m - 1 and y == n - 1:
                return 1

            if (x, y) in dp:
                return dp[(x, y)]

            dp[(x, y)] = util(x + 1, y) + util(x, y + 1)
            
            return dp[(x, y)]

        return util(0, 0)