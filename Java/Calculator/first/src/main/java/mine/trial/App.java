package mine.trial;

import java.util.Scanner;
import java.util.concurrent.ExecutionException;

import edu.princeton.cs.algs4.*;

/**
 * valid operation is +,-,*,/ with no sapce.
 */
public final class App {
    private Stack<String> ops = new Stack<>();// stack for oprator + - * / ( )
    private Stack<Double> vals = new Stack<>();// stack for values

    /**
     * 递归的方法：每次遇到一个左括号，进入递归，每次遇到右括号，返回主调函数 这样就可以每次只处理基本运算而不用管括号的影响了
     * 
     * @return
     */
    /*
     * public double calculate() { Scanner scan = new Scanner(System.in); while
     * (scan.hasNext()) { String s = scan.nextLine(); double v; if (s.equals("("))
     * return calculate(); else if (s.equals(")")) return v; } scan.close(); }
     */

    private void calculateMeetPlus() {
        String op;
        Double v1, v2;
        while (!ops.isEmpty() || ops.peek().equals("(")) {
            op = ops.pop();
            v1 = vals.pop();
            v2 = vals.pop();
            if (op.equals("+"))
                v1 += v2;
            else if (op.equals("-"))
                v1 -= v2;
            vals.push(v1);
        }
    }

    private void calculateMeetCloseParen() {
        String op = ops.pop();
        Double v1, v2;
        v1 = vals.pop();
        v2 = vals.pop();
        if (op.equals("+"))
            v1 += v2;
        else if (op.equals("-"))
            v1 -= v2;
        // 还有别的情况吗？
        vals.push(v1);
    }

    public App() {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        double v1, v2;
        while (!s.equals("=")) {
            if (s.equals("+") || s.equals("-")) {
                calculateMeetPlus();
                ops.push(s);
            } else if (s.equals("*") || s.equals("/") || s.equals("("))
                ops.push(s);
            else if (s.equals(")")) {
                calculateMeetCloseParen();
                ops.pop();
            } else {
                if (!ops.isEmpty()) {
                    String op = ops.peek();
                    if (op.equals("*")) {
                        ops.pop();
                        v1 = Double.parseDouble(s);
                        v2 = vals.pop();
                        v1 *= v2;
                        vals.push(v1);
                    } else if (op.equals("/")) {
                        ops.pop();
                        v1 = Double.parseDouble(s);
                        v2 = vals.pop();
                        v1 /= v2;
                        vals.push(v1);
                    }
                }
                else{
                    v1 = Double.parseDouble(s);
                    vals.push(v1);
                }
            }
            s = scan.nextLine();
        }
        scan.close();
    }

    /**
     * 辅助方法
     */
    public Double value() {
        Double v = vals.pop();
        return v;
    }

    /**
     * Says hello to the world.
     * 
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        App app = new App();
        System.out.println(app.value());
    }
}
