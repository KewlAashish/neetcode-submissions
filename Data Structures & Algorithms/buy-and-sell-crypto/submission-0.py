class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        ans = 0
        start = prices[l]

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            else:
                ans = max(ans, prices[r] - prices[l])
                r += 1

        return ans