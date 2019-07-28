package m.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * constructMaximumBinaryTree
 */
public class constructMaximumBinaryTreeSolution {

    private int indexOfMax(int[] nums, int i, int j) {
        int max = nums[i];
        int index = i;
        for (int k = i + 1; k < j; k++) {
            if (max < nums[k]) {
                max = nums[k];
                index = k;
            }
        }
        return index;
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return constructMaximumBinaryTree(nums, 0, nums.length);
    }

    private TreeNode constructMaximumBinaryTree(int[] nums, int i, int j) {
        TreeNode root;
        if (i < j - 1) {
            int index = indexOfMax(nums, i, j);
            root = new TreeNode(nums[index]);
            root.left = constructMaximumBinaryTree(nums, i, index);
            root.right = constructMaximumBinaryTree(nums, index + 1, j);
        } else if (i == j - 1) {
            root = new TreeNode(nums[i]);
            root.left = null;
            root.right = null;
        } else {
            root = null;
        }
        return root;
    }

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        // assert (input.length() >= 2);
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for (int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static String treeNodeToString(TreeNode root) {
        if (root == null) {
            return "[]";
        }

        String output = "";
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();

            if (node == null) {
                output += "null, ";
                continue;
            }

            output += String.valueOf(node.val) + ", ";
            nodeQueue.add(node.left);
            nodeQueue.add(node.right);
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);

            TreeNode ret = new constructMaximumBinaryTreeSolution().constructMaximumBinaryTree(nums);

            String out = treeNodeToString(ret);

            System.out.print(out);
        }
    }
}