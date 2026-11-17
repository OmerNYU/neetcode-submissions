# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Notes:

# At every node we calculate maximum path passing through node (can use both branches)

# Use the previous operation to update global maximum, returned to parent(only one branch is chosen)

# Use postorder dfs: left, right, root

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            leftgain = max(0, dfs(node.left))
            rightgain = max(0, dfs(node.right))

            path_sum = node.val + leftgain + rightgain

            res = max(res, path_sum)
            return node.val + max(leftgain, rightgain)
        
        dfs(root)
        return res
        

