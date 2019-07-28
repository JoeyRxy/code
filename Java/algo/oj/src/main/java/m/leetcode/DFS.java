package m.leetcode;

import java.util.Random;
import java.util.Stack;

import edu.princeton.cs.algs4.Graph;

/**
 * DFS
 */
public class DFS {

    private Graph g;

    public DFS(int N) {
        g = new Graph(N);
        Random r = new Random();
        for (int i = 0; i < N; i++) {
            g.addEdge(i, Math.abs(r.nextInt() % N));
        }
    }

    public void visit(int v) {
        System.out.println("vertex:" + v);
    }
    
    public void dfs() {
        Stack<Integer> s = new Stack<>();
        
    }
}