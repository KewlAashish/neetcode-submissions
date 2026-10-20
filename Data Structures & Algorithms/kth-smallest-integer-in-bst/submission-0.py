# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, node, result):
        if not node:
            return

        # if len(result) == k - 1

        self.util(node.left, result)
        result.append(node.val)
        self.util(node.right, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        self.util(root, result)

        return result[k - 1]