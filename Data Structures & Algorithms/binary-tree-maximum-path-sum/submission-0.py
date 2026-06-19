# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return float("-inf"), 0

            left_global, left_branch = dfs(node.left)
            right_global, right_branch = dfs(node.right)

            left_branch = max(left_branch, 0)
            right_branch = max(right_branch, 0)

            current_split = node.val + left_branch + right_branch
            current_global = max(left_global, current_split, right_global)

            current_branch_max = node.val + max(left_branch, right_branch)
            return current_global, current_branch_max
        output,_ = dfs(root)
        return output
