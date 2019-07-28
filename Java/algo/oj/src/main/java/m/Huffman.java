package m;

import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;

/**
 * Huffman
 * <p>
 * 不支持自定义的码元数组，只能是0,1,2,...,r
 */
public class Huffman {

    /**
     * Node
     */
    class Node {

        String symbol;
        double probability;
        Node[] offspring;
        // Node parent;

        Node() {
        }

        Node(String s, double p) {
            symbol = s;
            probability = p;
            offspring = null;
        }
    }

    class NodeCompare implements Comparator<Node> {

        public int compare(Node o1, Node o2) {
            double x = o1.probability - o2.probability;
            if (x > 0)
                return 1;
            else if (x == 0)
                return 0;
            else
                return -1;
        }

    }

    class Pair {
        String symbol;
        String code;

        Pair() {
        }

        Pair(String symbol, String code) {
            this.symbol = symbol;
            this.code = code;
        }
    }

    private Node huffmanTree;
    private int radix;
    private int len;
    private String[] symbols;
    private double[] probability;

    private HashMap<String, String> codebook;

    /**
     * 
     * @param symbols
     * @param probability
     * @param r           所用的码元个数
     */
    public Huffman(String[] symbols, double[] probability, int r) {
        if (r < 2)
            throw new IllegalArgumentException("基本码元数目必须大于等于2");
        if (symbols.length != probability.length)
            throw new IllegalArgumentException("Symbols\' length must agree with probability's length");
        this.len = symbols.length;
        this.radix = r;
        this.symbols = symbols;
        this.probability = probability;
        huffmanTree = build();
        codebook = new HashMap<>();
        getCode(huffmanTree, "");
    }

    public Huffman(double[] probability) {
        this.radix = 2;
        this.len = probability.length;
        this.probability = probability;
        this.symbols = new String[len];
        for (int i = 0; i != len; i++)
            symbols[i] = Integer.toString(i);

        huffmanTree = build();
        codebook = new HashMap<>();
        getCode(huffmanTree, "");
    }

    public Huffman(double[] probability, int r) {
        this.radix = r;
        this.len = probability.length;
        this.probability = probability;
        this.symbols = new String[len];
        for (int i = 0; i != len; i++)
            symbols[i] = Integer.toString(i);

        huffmanTree = build();
        codebook = new HashMap<>();
        getCode(huffmanTree, "");
    }

    private Node build() {
        Node[] nodes = new Node[len];
        for (int i = 0; i != len; i++)
            nodes[i] = new Node(symbols[i], probability[i]);
        PriorityQueue<Node> pq = new PriorityQueue<>(len, new NodeCompare());
        for (int i = 0; i != len; i++)
            pq.add(nodes[i]);
        // 建树
        boolean isOver = false;
        double sum;
        Node p;
        while (!isOver) {
            p = new Node();
            p.offspring = new Node[radix];
            sum = 0;
            for (int i = 0; i != radix; i++) {
                if (pq.isEmpty()) {
                    isOver = true;
                    break;
                }
                p.offspring[i] = pq.poll();
                sum += p.offspring[i].probability;
            }
            if (pq.isEmpty())
                isOver = true;
            p.probability = sum;
            pq.add(p);
        }
        Node tmp = pq.poll();
        if (Math.abs(tmp.probability - 1) > 10e-5)
            throw new IllegalArgumentException("总概率和不为1！");
        else
            return tmp;
    }

    /**
     * 
     * @param node
     * @param idx  parent Node's offsprint[idx]
     */
    public void getCode(Node node, String idx) {
        if (node == null)
            return;
        if (node.offspring == null) {
            codebook.put(node.symbol, idx);
            return;
        }
        for (int i = 0; i != radix; i++) {
            getCode(node.offspring[i], idx + Integer.toString(i));
        }
    }

    public String code(String text) {
        StringBuffer tmp = new StringBuffer();
        for (int i = 0; i != text.length(); i++) {
            tmp.append(codebook.get(text.substring(i, i + 1)));
        }
        return tmp.toString();
    }

    public static double[] getFreq(String text) {
        double[] freq = new double[256];
        int length = text.length();
        for (int i = 0; i != length; i++) {
            freq[text.charAt(i)]++;
        }
        for (int i = 0; i != 256; i++) {
            freq[i] /= length;
        }
        return freq;
    }

    public String decode(String codes, int radix) {
        char[] arr = codes.toCharArray();
        Node r = huffmanTree;
        StringBuffer tmp = new StringBuffer();
        try {
            for (int i = 0; i != arr.length; i++) {
                if (r.offspring == null) {// 到达叶子
                    tmp.append(r.symbol);
                    r = huffmanTree;
                    continue;
                }
                r = r.offspring[i];
            }
        } catch (NullPointerException e) {
            e.printStackTrace();
            System.out.println("this codes string has not coded right.");
        }
        return tmp.toString();
    }

    public String codeOf(String symbol) {
        return codebook.get(symbol);
    }

    public void printCodeBook() {
        for (String key : codebook.keySet())
            System.out.println(key + " : " + codebook.get(key).toString());
    }

    public static void main(String[] args) {
        double[] p = { 0.343, 0.149, 0.147, 0.145, 0.063, 0.063, 0.063, 0.027 };
        // String[] symbols = { "a", "b", "c", "d" };
        Huffman t = new Huffman(p);
        t.printCodeBook();
    }
}