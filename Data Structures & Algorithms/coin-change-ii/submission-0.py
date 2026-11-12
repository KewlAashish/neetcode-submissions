class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        pick:
            - increase ind
            - not increase ind
        not-pick: 
            - increase ind
        """
        n = len(coins)
        dp = {}

        def util(ind, amount_left):
            if amount_left == 0:
                return 1

            if amount_left < 0 or ind == n:
                return 0

            case = (ind, amount_left)
            if case in dp:
                return dp[case]

            possible = util(ind, amount_left - coins[ind]) + util(ind + 1, amount_left)

            dp[case] = possible
            
            return possible

        return util(0, amount)