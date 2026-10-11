class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for ch in s1:
            freq1[ch] += 1

        l = 0
        n1 = len(s1)
        n2 = len(s2)

        for r in range(n2):
            ch = s2[r]

            freq2[ch] += 1

            if r - l + 1 < n1:
                continue
            
            if freq1 == freq2:
                return True
            else:
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1

        return False    