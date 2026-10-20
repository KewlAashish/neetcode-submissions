# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, node, cache, ans):
        if not node:
            return

        if node in cache:
            return cache[node]

        """
            p1 = l + r + curr
            p2 = l + curr
            p3 = r + curr
        """

        self.util(node.left, cache, ans)
        self.util(node.right, cache, ans)

        p1, p2, p3 = node.val, node.val, node.val

        if node.left and node.right:
            p1 += cache[node.left] + cache[node.right]
    
        if node.left:
            p2 += cache[node.left]

        if node.right:
            p3 += cache[node.right]

        cache[node] = max(p1, max(p2, max(p3, node.val)))
        ans = max(ans, cache[node])

        return ans
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best complete path passing through this node
            ans = max(ans, node.val + left + right)

            # Best path that can extend to the parent
            return node.val + max(left, right)

        dfs(root)
        return ans

        