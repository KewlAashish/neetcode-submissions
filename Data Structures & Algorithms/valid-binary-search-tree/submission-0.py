# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_valid_bst_util(self, node, max_till_now, min_till_now):
        if not node:
            return True

        if node.val >= max_till_now or node.val <= min_till_now:
            return False
        
        left = self.is_valid_bst_util(node.left, node.val, min_till_now)
        right = self.is_valid_bst_util(node.right, max_till_now, node.val)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst_util(root, float("inf"), float("-inf"))