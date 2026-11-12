class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        add?
        subtract?
        """

        n = len(nums)
        dp = {}

        def util(ind, curr_sum):
            if ind == n:
                if curr_sum == target:
                    return 1
                
                return 0

            case = (ind, curr_sum)

            if case in dp:
                return dp[case]

            dp[case] = util(ind + 1, curr_sum - nums[ind]) + util(ind + 1, curr_sum + nums[ind])
            return dp[case]

        return util(0, 0)