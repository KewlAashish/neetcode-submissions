# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        if root == p or q? return root
        else:
            root.left has anything?
            root.right has anything?
            If yes then return the root

            If only one has something return whatever is returned from there
        """

        if not root:
            return root

        if root.val == p.val and root.val == q.val:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

        return None









