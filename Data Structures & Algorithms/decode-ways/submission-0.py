
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n

        def util(i):
            if i == n:
                return 1

            if s[i] == '0':
                return 0

            if dp[i] != -1:
                return dp[i]

            # Decode one digit
            count = util(i + 1)

            # Decode two digits
            if i + 1 < n:
                num = int(s[i:i + 2])

                if 10 <= num <= 26:
                    count += util(i + 2)

            dp[i] = count
            return count

        return util(0)
