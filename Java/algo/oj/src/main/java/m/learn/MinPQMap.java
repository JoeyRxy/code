package m.learn;



/**
 * MinPQMap
 * using a tree instead of an array.
 * 太复杂。因为插入一个元素最好的方法是在最后一个元素的右侧插入，而不是一直在左侧插入，所以最好还是用
 * 数组来表示，形成一个完全二叉树。
 */
public class MinPQMap<Key extends Comparable<Key>, Value> {


    class Node {
        Key key;
        Value value;
        Node parentNode;
        Node leftNode;
        Node rightnNode;

        Node() {
            parentNode = null;
            leftNode = null;
            rightnNode = null;
            key = null;
            value = null;
        }

        Node(Key key, Value value) {
            parentNode = null;
            leftNode = null;
            rightnNode = null;
            this.key = key;
            this.value = value;
        }
    }

    private Node root;
    private Node last;
    private int size;

    public MinPQMap() {
        root = last = new Node();
        size = 0;
    }
    
    private void exch(Node u,Node v) {
        Value tmpValue = u.value;
        Key tmpKey = u.key;
        u.value = v.value;
        u.key = v.key;
        v.value = tmpValue;
        v.key = tmpKey;
    }
    
    private void sink(Node node) {
        while (true) {
            if (node.leftNode.key.compareTo(node.key) < 0) {
                exch(node, node.leftNode);
                node = node.leftNode;
            }
            else if (node.rightnNode.key.compareTo(node.key) < 0) {
                exch(node, node.rightnNode);
                node = node.rightnNode;
            }
            else
                break;
        }
    }
    
    private void swim(Node node) {
        while (true) {
            if (node.parentNode == null) {
                break;
            }
            else if (node.parentNode.key.compareTo(node.key) > 0) {
                exch(node, node.parentNode);
                node = node.parentNode;
            }
            else {
                break;
            }
        }
    }

    public void insert(Key key,Value value) {
        if (last == root) {
            root.key = key;
            root.value = value;
        }
        else {
            
        }
    }
    
    /* public Node delMin() {

    } */

    public void change(Node node) {

    }
    
    /* public boolean isEmpty() {
        
    } */
    public static void main(String[] args) {
        MinPQMap<Double, String> pq = new MinPQMap<>();

    }
}