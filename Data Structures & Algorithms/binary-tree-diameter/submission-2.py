# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple(int,int):
            if not node:
                return (0,0)
            
            left_diameter, left_depth = dfs(node.left)
            right_diameter, right_depth = dfs(node.right)

            current_max_diameter = left_depth + right_depth
            global_max_diameter = max(left_diameter, right_diameter, current_max_diameter)
            current_depth = 1 + max(left_depth, right_depth)
            return (global_max_diameter, current_depth)
        final_diameter,_ = dfs(root)
        return final_diameter