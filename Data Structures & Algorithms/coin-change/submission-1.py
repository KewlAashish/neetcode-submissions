
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def util(amount_left):
            if amount_left == 0:
                return 0

            if amount_left < 0:
                return float("inf")

            if dp[amount_left] != -1:
                return dp[amount_left]

            min_coins = float("inf")

            for coin in coins:
                result = 1 + util(amount_left - coin)
                min_coins = min(min_coins, result)

            dp[amount_left] = min_coins
            return min_coins

        answer = util(amount)

        return -1 if answer == float("inf") else answer
