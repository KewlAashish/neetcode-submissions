class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [float("inf")] * (n + 1)
        max_dp = [float("-inf")] * (n + 1)

        answer = nums[0]

        for i in range(n):
            if i == 0:
                min_dp[i] = nums[i]
                max_dp[i] = nums[i]
                continue

            max_possible = max(nums[i], max(min_dp[i - 1]*nums[i], max_dp[i - 1]*nums[i]))
            min_possible = min(nums[i], min(min_dp[i - 1]*nums[i], max_dp[i - 1]*nums[i]))

            min_dp[i] = min_possible
            max_dp[i] = max_possible

            answer = max(answer, max_possible)

        return answer

        """
        -3, -2, 5

        minimum product at -3 = -3
        max product at -3 = -3

        -2
        possible answer = max_product before this -3* -2 = 6
        or min_product before this -3*-2 = 6
        or min[-2] = -2
        max[-2] = 6

        5
        possible answer = 6 * 5 or -2*5 or 5 = 30
        max[curr] = max(6*5, -2*5 or 5) = 30
        min[curr] = min(6*5, -2*5 or 5) = -10
        """