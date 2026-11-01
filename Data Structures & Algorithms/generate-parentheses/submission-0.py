class Solution:
    def util(self, open_, closed, s, results):
        if open_ == 0 and closed == 0:
            results.append(s)
            return

        if open_ == closed:
            # Case 1: We can never allow the closed braces to be used more than open ones
            self.util(open_ - 1, closed, s + "(", results)
            return
        
        if open_ > 0:
            # Case 2: If we still have some open left try it
            self.util(open_ - 1, closed, s + "(", results)

        # Case 3: Using the closed bracket
        self.util(open_, closed - 1, s + ")", results)

    def generateParenthesis(self, n: int) -> List[str]:
        """
        if we have some open braces left in the bank then use it or not use it, but if we dont have then then just add the closing braces till the length <= n*2
        """

        results = []

        self.util(n, n, "", results)

        return results