class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        for ch in s:
            if ch in s_hash:
                s_hash[ch] += 1
            else:
                s_hash[ch] = 1

        for ch in t:
            if ch not in s_hash or s_hash[ch] == 0:
                return False
            
            s_hash[ch] -= 1

        for ch in s:
            if s_hash[ch] > 0:
                return False

        return True