class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        ind_1
        ind_2

        if s1[ind1] == s2[ind2]:
            ind1 += 1
            ind2 += 1
        """

        n1 = len(text1)
        n2 = len(text2)
        dp = {}
        
        def util(ind1, ind2):
            if ind1 >= n1:
                return 0

            if ind2 >= n2:
                return 0

            if (ind1, ind2) in dp:
                return dp[(ind1, ind2)]

            count = 0

            if text1[ind1] == text2[ind2]:
                count = 1 + util(ind1 + 1, ind2 + 1)
            
            count = max(count, max(util(ind1 + 1, ind2), util(ind1, ind2 + 1)))
            dp[(ind1, ind2)] = count
            
            return count

        return util(0, 0)