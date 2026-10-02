# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        max_val = root.val - 1
        
        def dfs(root: TreeNode, max_val: int):
            result = 0

            if root is None:
                return 0
            elif root.val >= max_val:
                result += 1

            result += dfs(root.left, max(max_val, root.val))
            result += dfs(root.right, max(max_val, root.val))
            
            return result

        
        return dfs(root, max_val)

