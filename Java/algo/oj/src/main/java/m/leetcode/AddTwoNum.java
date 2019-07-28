package m.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * AddTwoNum
 */
public class AddTwoNum {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int c = 0;
        int sum = 0;
        ListNode ans = new ListNode(-1);
        ListNode tmp = ans;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                sum = l2.val + c;
                l2 = l2.next;
            } else if (l2 == null) {
                sum = l1.val + c;
                l1 = l1.next;
            } else {
                sum = l1.val + l2.val + c;
                l1 = l1.next;
                l2 = l2.next;
            }
            c = sum / 10;
            sum = sum % 10;
            tmp.next = new ListNode(sum);
            tmp = tmp.next;
        }
        if (c != 0) {
            tmp.next = new ListNode(c);
        }
        ans = ans.next;
        return ans;
    }

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
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

    public static ListNode stringToListNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);

        // Now convert that list into linked list
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for (int item : nodeValues) {
            ptr.next = new ListNode(item);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static String listNodeToString(ListNode node) {
        if (node == null) {
            return "[]";
        }

        String result = "";
        while (node != null) {
            result += Integer.toString(node.val) + ", ";
            node = node.next;
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            ListNode l1 = stringToListNode(line);
            line = in.readLine();
            ListNode l2 = stringToListNode(line);

            ListNode ret = new AddTwoNum().addTwoNumbers(l1, l2);

            String out = listNodeToString(ret);

            System.out.print(out);
        }
    }
}