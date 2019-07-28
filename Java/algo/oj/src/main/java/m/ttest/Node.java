package m.ttest;

/**
 * Node
 */
public class Node<T> {

    public T val;
    public int index;

    public Node(T val, int index) {
        this.index = index;
        this.val = val;
    }

    public Node() {
    }
}