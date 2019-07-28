package m.using;

import edu.princeton.cs.algs4.Queue;

//import edu.princeton.cs.algs4.StdIn;

/**
 * <h4>SuffixTree</h4>
 * <p>
 * <code>$</code> for ending.
 * </p>
 * 
 * <p>
 * example:
 * </p>
 * <code>s = "xyzxyaxyz$"</code>
 * 
 * <p>
 * I dont understand why there is a "index" for every leaf node?
 * </p>
 */
public class SuffixTree {
    /**
     *
     */

    // private static final int _0 = 0;
    private String s;
    private Vertex_Suffix root;

    public SuffixTree(String s) {
        this.s = s + '$';
        root = new Vertex_Suffix();
        Brute();
    }

    /**
     * pseuocode: <code>
     *  if there is not a path from root to s[i]: 
     *      create a new branch s[i...s.length()] 
     *  else: 
     *      fork a new branch split from the diff
     * </code>
     */
    public void Brute() {
        // let s = "xyzxyaxyz$"
        int n = s.length();
        for (int i = n - 1; i >= 0; i--) {
            dfs(root, s.substring(i));
        }
    }

    /**
     * 
     * @param key
     * @return index in the
     */
    public int search(String key) {
        int n = key.length();
        for (int i = 0; i < n; i++) {
            Vertex_Suffix t = root;
        }
        return 0;
    }

    /**
     * No marked[],for there's no cycle path about the flag <code>isOver</code>
     */
    public void dfs(Vertex_Suffix r, String key) {
        /*
         * if (isOver) return;
         */
        // boolean notFind = true;
        for (Vertex_Suffix child : r.offspring()) {
            /*
             * if (isOver)//TODO:这个isOver变量为什么在返回主调函数的时候会变回原来的值呢？不能实现逐层跳出的结构了……即使isOver是封装类，
             * 该对象是引用啊…… return;
             */
            String tmpString = child.s();// r->child路径上的字符串
            char c = tmpString.charAt(0);
            if (c == key.charAt(0)) {
                int i;
                int len = tmpString.length();
                for (i = 1; i < len; i++) {// 判断有多少一样，并从不同的部分分支成新子树
                    if (tmpString.charAt(i) != key.charAt(i)) {
                        child.change(key.substring(0, i));// s.substring(a,b) return s[a,b)
                        child.addChild(tmpString.substring(i));
                        child.addChild(key.substring(i));
                        // isOver = true;
                        return;// ATTENTION：不用费心弄什么标志位；既然已经完成任务，直接返回即可
                    }
                }
                // notFind = false;
                /*
                 * if (isOver) return;
                 */
                if (i == len) {
                    dfs(child, key.substring(len));
                    // notFind = false;
                    return;// ATTENTION:在dfs递归返回的时候，一定是已经完成了任务，所以主次结束就可以了
                }
            }
        }
        r.addChild(key);// ATTENTION：为什么不用设之前的notFind 标志位呢？对应于前面 “但凡完成任务就return”的设计，这里只需根据foreach
                        // child:offspring这个循环是否结束就可以知道是否找在root下找到了可以匹配的路径
    }

    public void show() {
        show(root);
    }

    /**
     * 层序遍历显示suffix tree 希望能够层序输出——每一层单行显示
     * <a href="https://rosettacode.org/wiki/Visualize_a_tree#Java">how to visualize
     * a tree? </a>
     * 
     * @param r
     * @return
     */
    private void show(Vertex_Suffix r) {
        System.out.println("层序输出，每层一行，不同父节点的节点之间用 \'|\'隔开");
        // List<String> ans = new ArrayList<>();
        Queue<Vertex_Suffix> q = new Queue<>();
        int curLayerCount = 1;// current layer node count
        int nextLayerCount = 0;// next layer node count
        q.enqueue(r);
        System.out.println("root");
        while (!q.isEmpty()) {
            curLayerCount--;
            Vertex_Suffix tmp = q.dequeue();
            for (Vertex_Suffix v : tmp.offspring()) {
                System.out.print(v.s() + '\t');
                q.enqueue(v);
                nextLayerCount++;
            }
            System.out.print('|');
            if (curLayerCount == 0) {
                System.out.print('\n');
                curLayerCount = nextLayerCount;
            }
        }
    }

    public static void main(String[] args) {
        String s = "banana";
        SuffixTree st = new SuffixTree(s);
        st.show();
    }
}