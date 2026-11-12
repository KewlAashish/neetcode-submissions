class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def util(prev, ind):
            if ind >= n:
                return 0

            case = (prev, ind)
            if case in dp:
                return dp[case]

            # buy
            buy, not_buy, sell = float("-inf"), float("-inf"), float("-inf")
            if prev == -1:
                buy = util(ind, ind + 1)

            # sell or skip?
            if prev != -1:
                sell = prices[ind] - prices[prev] + util(-1, ind + 2)
            
            not_buy = util(prev, ind+1)

            dp[case] = max(buy, max(sell, not_buy))

            return dp[case]

        return util(-1, 0)