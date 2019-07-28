package m.learn;

import edu.princeton.cs.algs4.MaxPQ;

/**
 * IndexMinPQm
 */
@SuppressWarnings("unused")
public class IndexMinPQm<Key extends Comparable<Key>> {
    private int N;
    private int maxN;
    private int[] pq;
    private int[] qp;
    private Key[] keys;

    public IndexMinPQm() {

    }

    public IndexMinPQm(int maxN) {
        N = 1;
        this.maxN = maxN;
        pq = new int[maxN];
        qp = new int[maxN]; // qp[i]
        keys = (Key[]) new Comparable[maxN]; // 此处的泛型数组转换必须使用Comparable吗？
        for (int i = 0; i < maxN; i++) {
            qp[i] = -1;
        }
    }

    private void expend() {

    }

    public void insert(int k, Key key) {
        keys[k] = key;

    }

    private int less() {
        return 0;
    }

    private void swim(int k) {

    }

    private void sink(int k) {

    }

}