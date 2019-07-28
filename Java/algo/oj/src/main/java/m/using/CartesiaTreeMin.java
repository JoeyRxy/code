package m.using;

import java.util.Stack;

import edu.princeton.cs.algs4.Queue;

/**
 * CartesiaTree minimum
 */
public class CartesiaTreeMin<T extends Comparable<T>> {

    private Stack<NodeCartesia<T>> s;
    private NodeCartesia<T> root;

    public CartesiaTreeMin(T[] a) {
        root = new NodeCartesia<T>();// the root now is a super root
        s = new Stack<>();
        int len = a.length;
        NodeCartesia<T>[] nodes = new NodeCartesia[len];// ATTENTION <-如何使用泛型类的数组！
        for (int i = 0; i < len; i++) {
            nodes[i] = new NodeCartesia<>(a[i], i);
        }
        s.push(nodes[0]);
        nodes[0].pNode = root;
        root.rNode = nodes[0];
        NodeCartesia<T> tmp = nodes[0];
        NodeCartesia<T> last = null;
        // TODO 代码很乱，逻辑很乱，不清晰
        for (int i = 1; i < len; i++) {
            NodeCartesia<T> cur = nodes[i];
            while (!s.isEmpty() && tmp.val.compareTo(cur.val) > 0)
                tmp = s.pop();// you pop a node but don't know if it's val > cur.val or s is empty,so
            if (tmp.val.compareTo(cur.val) > 0 && s.isEmpty())// ATTENTION 不光得是空栈，而且保证刚刚弹出的元素是<=当前元素，否则tmp还是刚刚弹出的元素
                tmp = root;// set to super root
            last = tmp.rNode;
            if (last != null) {// if have poped out some nodes
                cur.lNode = last;// link nodes pop out to cur.lNode
                last.pNode = cur;
            }
            cur.pNode = tmp;// link cur to tmp.rNode
            tmp.rNode = cur;

            s.push(cur);
            tmp = cur;// set to s.peek() for next comparision
        }
        root = root.rNode;
    }

    public void inOrder() {
        inOrder(root);
    }

    public void inOrder(NodeCartesia<T> r) {
        if (r != null) {
            inOrder(r.lNode);
            System.out.print(r.val + "\t");
            inOrder(r.rNode);
        }
    }

    public void levelOrder() {
        Queue<NodeCartesia<T>> q = new Queue<>();
        q.enqueue(root);
        NodeCartesia<T> tmp;
        q.enqueue(null);// FLAG!
        while (!q.isEmpty()) {
            tmp = q.dequeue();
            if (tmp == null) {
                q.enqueue(null);
                System.out.print('\n');
                if (q.size() <= 1)// ATTENTION
                    break;
                continue;
            }
            System.out.print(tmp.val + "\t");
            if (tmp.lNode != null)
                q.enqueue(tmp.lNode);
            if (tmp.rNode != null)
                q.enqueue(tmp.rNode);
        }
    }

    public void level() {
        Queue<NodeCartesia<T>> q = new Queue<>();
        q.enqueue(root);
        NodeCartesia<T> tmp;
        while (!q.isEmpty()) {
            tmp = q.dequeue();
            System.out.print(tmp.val);
            if (tmp.lNode != null)
                q.enqueue(tmp.lNode);
            if (tmp.rNode != null)
                q.enqueue(tmp.rNode);
        }
    }

    public static void main(String[] args) {
        Integer[] a = { 3, 2, 4, 5, 6, 8, 1, 9, 10, 7 };
        CartesiaTreeMin<Integer> t = new CartesiaTreeMin<>(a);
        t.inOrder();
        System.out.print('\n');
        t.levelOrder();
    }
}