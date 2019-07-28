package m.using;

class NodeCartesia<T extends Comparable<T>> {

    NodeCartesia<T> pNode;
    NodeCartesia<T> lNode, rNode;
    T val;
    int index;

    public NodeCartesia(NodeCartesia<T> p, NodeCartesia<T> l, NodeCartesia<T> r, T v, int i) {
        pNode = p;
        lNode = l;
        rNode = r;
        val = v;
        index = i;
    }

    public NodeCartesia() {
    }

    public NodeCartesia(T val, int index) {
        this.index = index;
        this.val = val;
    }
}