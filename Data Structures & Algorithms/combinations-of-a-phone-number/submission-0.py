class Solution:

    def utils(self, ind, s, digits, results):
        
        abc_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        if ind == len(digits):
            if s:
                results.append(s)
            return

        for ch in abc_map[digits[ind]]:
            self.utils(ind + 1, s + ch, digits, results)

        return

    def letterCombinations(self, digits: str) -> List[str]:
        results = []

        self.utils(0, "", digits, results)

        return results