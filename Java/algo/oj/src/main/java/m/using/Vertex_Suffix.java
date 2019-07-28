package m.using;

import java.util.ArrayList;
import java.util.List;

/**
 * Vertex_Suffix
 * 
 * @param p         parent of this vertex
 * @param s         当前节点到父节点上的边上的字符串
 * @param index     if it's leaf node,it indicates the index of this suffix;elif
 *                  -2 for root;else -1
 * @param offspring 类型：<code>List&lt;Vertex_Suffix&gt; </code>
 */
public class Vertex_Suffix {

    // private int index = -1;
    private Vertex_Suffix p;
    /**
     * 当前节点到父节点上的边上的字符串
     */
    private String s;
    /**
     * 类型：<code>List&lt;Vertex_Suffix&gt; </code>
     */
    private List<Vertex_Suffix> offspring;

    /*
     * public Vertex_Suffix(int v) { offspring = new ArrayList<>(); index = v; }
     */

    public Vertex_Suffix() {
        offspring = new ArrayList<>();
    }

    public Vertex_Suffix(/* int index,  */Vertex_Suffix p, String s) {
        // this.index = index;
        this.p = p;
        this.s = s;
        offspring = new ArrayList<>();
    }

    public List<Vertex_Suffix> offspring() {
        return offspring;
    }

    public void addChild(/* int v, */ String s) {
        Vertex_Suffix t = new Vertex_Suffix(this, s);
        offspring.add(t);
    }

    public void change(String s) {
        this.s = s;
    }

    public String s() {
        return s;
    }   

}