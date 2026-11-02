class Solution:

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def util(self, left_ind, ind, s, results, curr):

        if ind == len(s):
            if left_ind == len(s):
                results.append(curr)
            return

        # Option 1: Partition at current index
        if self.is_palindrome(s[left_ind:ind + 1]):
            self.util(
                ind + 1,
                ind + 1,
                s,
                results,
                curr + [s[left_ind:ind + 1]]
            )

        # Option 2: Extend current substring
        self.util(left_ind, ind + 1, s, results, curr)

    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.util(0, 0, s, results, [])
        return results