class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = l
        ans = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                ans = max(ans, r - l + 1)
                r += 1
            else:
                ans = max(ans, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

                seen.add(s[r])
                r += 1

        return ans