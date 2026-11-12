class Solution:
    def util(self, prev, curr, s, wordDict, dp):
        if curr == len(s):
            if prev == curr:
                return True
            else:
                return False

        if dp[prev][curr] != float("inf"):
            return dp[prev][curr]

        curr_word = s[prev: curr + 1]

        possible = False

        if curr_word in wordDict:
            possible = possible | self.util(curr + 1, curr + 1, s, wordDict, dp)
        
        possible = possible | self.util(prev, curr + 1, s, wordDict, dp)

        dp[prev][curr] = possible

        return possible
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        prev = 0
        curr = 0

        curr_word = s[prev:curr + 1]

        is curr_word part of wordDict?
        If yes,
            - Let use this word, and make prev = curr + 1 and curr = curr + 1? If returns true, return true
            - Maybe instead of using lets push this further to see if we can form a bigger word later on? If returns True, return true
        If no,
            - Try calling, prev = prev but curr = curr + 1? If true, return true
        
        if no trues,
        return False?
        """

        wordDict = set(wordDict)
        n = len(s)
        dp = [[float("inf")] * n for _ in range(n)]

        prev = 0
        curr = 0

        return self.util(prev, curr, s, wordDict, dp) == 1