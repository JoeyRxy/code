package mine.trial;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

/**
 * trial
 */
public class trial {
    public static boolean isNumber(char c) {
        return c >= 48 && c <= 57;
    }
    public static void main(String[] args) {
        String x = StdIn.readLine();
        for (int i = 0; i < x.length(); i++) {
            if(isNumber(x.charAt(i)))
                StdOut.print(x.charAt(i));
        }
    }
}