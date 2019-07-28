package m.leetcode;

import java.util.Random;

/**
 * BiTree
 */
public class BiTree {

    TreeNode root;

    public BiTree() {

    }

    public void visit(TreeNode node) {
        System.out.println("node:" + node.val);
    }

    public void dfsReccusive_Pre(TreeNode root) {
        if (root != null) {
            visit(root);
            dfsReccusive_Pre(root.left);
            dfsReccusive_Pre(root.right);
        }
    }

    public static void main(String[] args) {
        Random r = new Random();
        int maxN = 10;
        for (int i = 0; i < maxN; i++) {

        }
    }
}