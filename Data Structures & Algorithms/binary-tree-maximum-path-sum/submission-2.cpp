/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int global_max = INT_MIN;
        dfs(root, global_max);
        return global_max;
    }
private:
    int dfs(TreeNode* node, int& global_max) {
        if (!node) {
            return 0;
        }

        int left_branch = std::max(0, dfs(node->left, global_max));
        int right_branch = std::max(0, dfs(node->right, global_max));
        global_max = std::max(global_max, node->val + left_branch + right_branch);
        return node->val + std::max(left_branch, right_branch);
    }
};
