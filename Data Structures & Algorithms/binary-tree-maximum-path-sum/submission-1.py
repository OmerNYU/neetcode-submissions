# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float("-inf")

        def dfs(node):

            nonlocal res

            if not node:
                return 0

            leftgain = max(0, dfs(node.left))
            rightgain = max(0, dfs(node.right))

            pathSum = node.val + leftgain + rightgain

            res = max(res, pathSum)

            return node.val + max(leftgain, rightgain)
        
        dfs(root)

        return res