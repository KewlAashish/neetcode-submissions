
class Solution:
    def util(self, curr, end, nums, dp):
        if curr >= end:
            return 0

        if dp[curr] != -1:
            return dp[curr]

        take_1 = self.util(curr + 2, end, nums, dp)
        take_2 = self.util(curr + 3, end, nums, dp)

        dp[curr] = nums[curr] + max(take_1, take_2)
        return dp[curr]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # Case A: Houses [0, n-2]
        dp1 = [-1] * n
        case_a = max(
            self.util(0, n - 1, nums, dp1),
            self.util(1, n - 1, nums, dp1)
        )

        # Case B: Houses [1, n-1]
        dp2 = [-1] * n
        case_b = max(
            self.util(1, n, nums, dp2),
            self.util(2, n, nums, dp2)
        )

        return max(case_a, case_b)
