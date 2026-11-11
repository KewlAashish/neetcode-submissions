
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def solve(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            take = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            dp[i] = max(take, skip)
            return dp[i]

        return solve(0)
