class Solution:

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True


    def util(self, left_ind, ind, s, results, curr):
        if ind == len(s):

            if s[left_ind:ind] and self.is_palindrome(s[left_ind:ind]):
                curr.append(s[left_ind:ind])
                results.append(curr)

            return

        # Using this index to partition:
        # Only possible is the left_ind till here ind + 1 is also a palindrome
        if self.is_palindrome(s[left_ind: ind + 1]):
            self.util(ind + 1, ind + 1, s, results, curr + [s[left_ind: ind + 1]])
        
        self.util(left_ind, ind + 1, s, results, curr)


    def partition(self, s: str) -> List[List[str]]:
        results = []

        self.util(0, 0, s, results, [])

        return results