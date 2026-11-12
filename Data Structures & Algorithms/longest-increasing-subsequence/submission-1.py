
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def util(prev, curr):
            if curr == n:
                return 0

            if (prev, curr) in dp:
                return dp[(prev, curr)]

            # Choice 1: Skip current element
            not_pick = util(prev, curr + 1)

            # Choice 2: Pick current element if valid
            pick = 0

            if prev == -1 or nums[curr] > nums[prev]:
                pick = 1 + util(curr, curr + 1)

            dp[(prev, curr)] = max(pick, not_pick)

            return dp[(prev, curr)]

        return util(-1, 0)
