/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode search = root;
        while (search != null) {
            if (search.val > val) {
                if (search.left == null) return null;
                search = search.left;
            } else if (search.val < val) {
                if (search.right == null) return null;
                search = search.right;
            } else {
                return search;
            }
        }
        return null;
    }
}