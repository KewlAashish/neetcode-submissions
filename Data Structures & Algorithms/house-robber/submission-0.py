class Solution:

    def util(self, curr, n, dp, nums):
        if curr >= n:
            return 0

        if dp[curr] != -1:
            return dp[curr]

        take_1 = self.util(curr + 2, n, dp, nums)
        take_2 = self.util(curr + 3, n, dp, nums)

        dp[curr] = nums[curr] + max(take_1, take_2)
        
        return dp[curr]

    def rob(self, nums: List[int]) -> int:
        """
        Looks like we can start at any house at any index
        Also, the next house shouldn't be just i - 2 or i + 2 right? We can pick anyone between 0 -> i - 2 and i + 2 -> n - 1

        In the end I belive there has to be a house either from index 0 or 1 in the best sequence possible. Because why would two consecutive houses
        be left out? Would be wrong to leave a house when you can actually use them

        So maybe this could be something like max(util(0), util(1))

        Now how to pick the next best house?
        Go like curr + 2 or curr + 3, because curr + 1 and curr + 2 both can be ideally skipped. Like in reality,
        curr + 3 has a better sequence overall and does not need curr + 1 and curr + 2
        """

        n = len(nums)
        dp = [-1] * (n)

        return max(self.util(0, n, dp, nums), self.util(1, n, dp, nums))