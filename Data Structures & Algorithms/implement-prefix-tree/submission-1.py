class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = True

class PrefixTree:

    def __init__(self):
        self.root = Node(0)
    
    def insert_util(self, root, ind, nodes_val):

        if ind == len(nodes_val):
            root.is_end = True
            return

        if nodes_val[ind] in root.children:
            self.insert_util(root.children[nodes_val[ind]], ind + 1, nodes_val)
        else:
            root.children[nodes_val[ind]] = Node(nodes_val[ind])
            root.children[nodes_val[ind]].is_end = False
            self.insert_util(root.children[nodes_val[ind]], ind + 1, nodes_val)

    def insert(self, word: str) -> None:
        # nodes_val = word.split("")
        self.insert_util(self.root, 0, word)

    def search_util(self, node, ind, word):
        if ind == len(word):
            return node.is_end

        if word[ind] in node.children:
            return self.search_util(node.children[word[ind]], ind + 1, word)

        return False

    def search(self, word: str) -> bool:
        return self.search_util(self.root, 0, word)


    def start_util(self, node, ind, word):
        if ind == len(word):
            return True

        if word[ind] in node.children:
            return self.start_util(node.children[word[ind]], ind + 1, word)

        return False

    def startsWith(self, prefix: str) -> bool:
        return self.start_util(self.root, 0, prefix)