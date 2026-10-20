# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, node, result, k):
        if not node:
            return

        self.util(node.left, result, k)

        if len(result) == k:
            return

        result.append(node.val)
        self.util(node.right, result, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        self.util(root, result, k)

        return result[-1]