class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node(0)
    
    def search_util(self, node, ind, word):
        if ind == len(word):
            return node.is_end

        ch = word[ind]

        if ch in node.children:
            return self.search_util(node.children[ch], ind + 1, word)
        
        return False

    def search(self, word):
        return self.search_util(self.root, 0, word)


    def starts_with_util(self, node, ind, word):
        if ind == len(word):
            return True, node

        ch = word[ind]

        if ch in node.children:
            return self.starts_with_util(node.children[ch], ind + 1, word)
        
        return False, None

    def starts_with(self, word):
        return self.starts_with_util(self.root, 0, word)

    def insert_util(self, node, ind, word):
        if ind == len(word):
            node.is_end = True
            return

        ch = word[ind]
        if ch in node.children:
            return self.insert_util(node.children[ch], ind + 1, word)

        new_node = Node(ch)
        node.children[ch] = new_node
        self.insert_util(new_node, ind + 1, word)
        
        return

    def insert(self, word):
        self.insert_util(self.root, 0, word)
        return

class Solution:

    def dfs(self, x, y, board, curr_word, words, trie, visited, results):
        if (x, y) in visited or (x >= len(board) or x < 0 or y >= len(board[0]) or y < 0):
            return

        ch = board[x][y]
        word = curr_word + ch

        is_present, end_node = trie.starts_with(word)
        
        if not is_present:
            return

        if is_present and end_node.is_end:
            results.add(word)

        visited.add((x, y))
        for moves in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(x + moves[0], y + moves[1], board, word, words, trie, visited, results)
        
        visited.remove((x, y))

        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        For starters, I feel given this has a word search feels, this has to be related to tries

        But the fact that we have implement a trie using a grid of characters would take a lot of time personally and seems like an
        in-efficient path to me

        DFS on the other hand for each word makes more sense to me, While DFS I can try cache some prefix and results in a trie
        So later on I can find the next word is already passed through?
        """

        trie = Trie()

        for word in words:
            trie.insert(word)

        x_max = len(board)
        y_max = len(board[0])
        
        results = set()

        for x in range(x_max):
            for y in range(y_max):
                self.dfs(x, y, board, "", words, trie, set(), results)

        return list(results)
            

