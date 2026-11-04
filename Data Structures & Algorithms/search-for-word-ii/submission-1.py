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

    def dfs(self, x, y, board, curr_word, trie_node, visited, results):

        # Boundary and visited checks
        if (
            x < 0 or x >= len(board)
            or y < 0 or y >= len(board[0])
            or (x, y) in visited
        ):
            return

        ch = board[x][y]

        # Prefix doesn't exist in Trie
        if ch not in trie_node.children:
            return

        # Move one level deeper in Trie
        next_node = trie_node.children[ch]
        word = curr_word + ch

        # Complete word found
        if next_node.is_end:
            results.append(word)
            next_node.is_end = False

        # Mark current board cell
        visited.add((x, y))

        # Explore all four directions
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(
                x + dx,
                y + dy,
                board,
                word,
                next_node,
                visited,
                results
            )

        # Backtrack
        visited.remove((x, y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()

        for word in words:
            trie.insert(word)

        results = []

        for x in range(len(board)):
            for y in range(len(board[0])):
                self.dfs(
                    x, y,
                    board,
                    "",
                    trie.root,
                    set(),
                    results
                )

        return results