class Solution:

    def util(self, curr, n, dp):
        if curr == n:
            return 1

        if curr > n:
            return 0

        if dp[curr] != -1:
            return dp[curr]

        dp[curr] = self.util(curr + 1, n, dp) + self.util(curr + 2, n, dp)

        return dp[curr]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n + 1)
        # starting with floor:
        # If n == 1, we can do only 1 possible way
        # if n == 2, we can do 2 possible ways

        return self.util(0, n, dp)