# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def good_nodes_util(self, node, max_till_now):
        count = 0

        if not node:
            return count

        if node.val >= max_till_now:
            count += 1

        max_till_now = max(max_till_now, node.val)

        count += self.good_nodes_util(node.left, max_till_now)
        count += self.good_nodes_util(node.right, max_till_now)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.good_nodes_util(root, float("-inf"))
        