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
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diameter = 0;

        auto dfs = [&](auto& self, TreeNode* curr) -> int {
            if (!curr){
                return 0;
            }
            int left_h = self(self, curr -> left);
            int right_h = self(self, curr -> right);
            
            max_diameter = std::max(max_diameter, left_h + right_h);
            return 1 + std::max(left_h, right_h);
        };
        dfs(dfs,root);
        return max_diameter;
    }
};

