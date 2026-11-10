class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        words = set(word_list)

        bfs = deque()

        bfs.append((begin_word, 1))
        if begin_word in words:
            words.remove(begin_word)

        def is_valid(a, b):
            if a == b:
                return True
            
            if len(a) != len(b):
                return False

            count = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1

                if count > 1:
                    return False

            return True

        while bfs:
            word, steps = bfs.popleft()
            
            if word == end_word:
                return steps

            for next_word in word_list:
                if next_word in words and is_valid(word, next_word):
                    words.remove(next_word)
                    bfs.append((next_word, steps + 1))

        return 0