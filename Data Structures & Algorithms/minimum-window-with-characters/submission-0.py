class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count_t = Counter(t)
        missing = len(t)


        best_start = 0
        best_len = float("inf")
        l = 0

        for r, ch in enumerate(s):
            if count_t[ch] > 0:
                missing -= 1

            count_t[ch] -= 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_start = l
                    best_len = r - l + 1
                
                count_t[s[l]] += 1
                if count_t[s[l]] > 0:
                    missing += 1

                l += 1

        return "" if best_len == float("inf") else s[best_start:best_start+best_len]