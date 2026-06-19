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
        auto result = dfs(root);
        return result.first;
    }
private:
    std::pair<int, int> dfs(TreeNode* node) {
        if (!node) {
            return {INT_MIN, 0};
        }

        auto left = dfs(node->left);
        auto right = dfs(node->right);

        int left_branch = std::max(left.second, 0);
        int right_branch = std::max(right.second, 0);

        int current_split_max = node->val + left_branch + right_branch;
        int current_global_max = std::max({left.first, right.first, current_split_max});
        int current_branch_max = node->val + std::max(left_branch, right_branch);

        return {current_global_max, current_branch_max};
    }
};
