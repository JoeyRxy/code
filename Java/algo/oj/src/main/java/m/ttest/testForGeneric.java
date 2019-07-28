package m.ttest;

//TODO : 没救了这个问题？怎么使用泛型数组？

/**
 * CartesiaTree minimum
 */
public class testForGeneric<T> {

    public testForGeneric(T[] a) {
        int len = a.length;
        Node<T>[] nodes = new Node[len];// should use Comparable rather than Object??
        for (int i = 0; i < len; i++) {
            nodes[i] = new Node<>(a[i], i);
        }
        for (int i = 0; i < len; i++) {
            System.out.print(nodes[i].val);
        }
    }

    public static void main(String[] args) {
        Integer[] a = { 3, 2, 4, 5, 6, 8, 9, 10, 7 };
        testForGeneric<Integer> t = new testForGeneric<>(a);
    }
}