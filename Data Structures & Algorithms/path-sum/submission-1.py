# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        def dfs(root, total):
            if not root:
                return False
            total += root.val
            if not root.left and not root.right:
                return total == targetSum
                
            left = dfs(root.left, total)
            right = dfs(root.right, total)
        
            return left or right
        return dfs(root, 0)