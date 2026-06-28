# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def vaild(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            left = vaild(node.left, left, node.val)
            right = vaild(node.right, node.val, right)

            return left and right
        
        return vaild(root, float("-inf"), float("inf"))