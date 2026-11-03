class Node:
    def __init__(self, val):
        self.val = val
        self.childrens = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node(0)
        return    

    def add_util(self, node, ind, word):
        if ind == len(word):
            node.is_end = True
            return

        ch = word[ind]

        if ch in node.childrens:
            self.add_util(node.childrens[ch], ind + 1, word)
        else:
            new_node = Node(ch)
            node.childrens[ch] = new_node
            self.add_util(new_node, ind + 1, word)

    def addWord(self, word: str) -> None:
        self.add_util(self.root, 0, word)
    
    def search_util(self, node, ind, word):
        if ind == len(word):
            return node.is_end

        if word[ind] == ".":
            for child, child_node in node.childrens.items():
                if self.search_util(child_node, ind + 1, word):
                    return True
        else:
            ch = word[ind]
            if ch in node.childrens:
                return self.search_util(node.childrens[ch], ind + 1, word)

        return False

    def search(self, word: str) -> bool:
        return self.search_util(self.root, 0, word)        
