class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opening_chars = {"(", "[", "{"}
        closing_chars = {")", "]", "}"}

        hash_map = {"}": "{", ")": "(", "]": "["}

        for ch in s:
            if ch in opening_chars:
                st.append(ch)
            
            if ch in closing_chars:
                open_ch = hash_map[ch]
                if st and st[-1] == open_ch:
                    st.pop()
                else:
                    return False

        return True if len(st) == 0 else False