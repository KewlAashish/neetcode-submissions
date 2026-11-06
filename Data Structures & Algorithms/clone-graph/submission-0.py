"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def util(self, node, prev_node, visited, hash):
        if not node or node in visited:
            return

        new_node = Node(node.val)
        hash[node] = new_node
        prev_node.neighbors.append(new_node)
        visited.add(node)

        for child in node.neighbors:
            if child not in hash:
                self.util(child, new_node, visited, hash)
            else:
                new_node.neighbors.append(hash[child])


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        dummy_head = Node(0)
        visited = set()
        hash = {}
        self.util(node, dummy_head, visited, hash)

        return None if not dummy_head.neighbors[0] else dummy_head.neighbors[0]