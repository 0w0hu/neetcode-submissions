# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if right:    
                res.append(right)

        return res