class Solution:
    def util(self, curr, n, dp, cost):
        if curr >= n:
            return 0

        if dp[curr] != -1:
            return dp[curr]

        dp[curr] = cost[curr] + min(self.util(curr + 1, n, dp,cost), self.util(curr + 2, n, dp, cost))

        return dp[curr]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n)

        return min(self.util(0, n, dp, cost), self.util(1, n, dp, cost))