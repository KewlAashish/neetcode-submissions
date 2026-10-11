class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            s_word = tuple(sorted(word))
            if s_word in anagram_map:
                anagram_map[s_word].append(word)
            else:
                anagram_map[s_word] = [word]
        
        return list(anagram_map.values())