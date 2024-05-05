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
    static ArrayList<Integer> list1 = new ArrayList<>();
    static ArrayList<Integer> list2 = new ArrayList<>();
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        
        build(root1, list1);
        build(root2, list2);
        
        return list1.equals(list2);
    }
    
    static void build(TreeNode node, ArrayList<Integer> list) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            list.add(node.val);
            return;
        }
        
        build(node.left, list);
        build(node.right, list);
    }
}