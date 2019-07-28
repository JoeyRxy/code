package m.using;

/**
 * @deprecated
 * Edge_Suffix
 */
public class Edge_Suffix {

    private String s;
    private Vertex_Suffix from;
    private Vertex_Suffix to;

    /* public Edge_Suffix() {
        from = new Vertex_Suffix(-1);
        to = new Vertex_Suffix(-1);
        s = null;
    } */

    public Edge_Suffix(Vertex_Suffix from, Vertex_Suffix to, String s) {
        this.from = from;
        this.to = to;
        this.s = s;
    }

    public Vertex_Suffix from() {
        return from;
    }
    
    public Vertex_Suffix to() {
        return to;
    }

    public String s() {
        return s;
    }

    public String toString() {
        if (s.equals("$")) {
            return null;
        }
        return s.substring(0, s.length() - 2);
    }
}