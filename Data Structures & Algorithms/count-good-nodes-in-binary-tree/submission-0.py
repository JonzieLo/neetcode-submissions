# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_v):
            if not node: return 0

            output = 1 if node.val >= max_v else 0
            max_v = max(max_v, node.val)
            output += dfs(node.left, max_v)
            output += dfs(node.right, max_v)
            return output
        return dfs(root, root.val)