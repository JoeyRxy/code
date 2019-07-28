package mine.trial;
import edu.princeton.cs.algs4.*;
/**
 * CalculateString
 */
public class CalculateString {
    private Stack<String> ops = new Stack<>();
    private Stack<Double> vals = new Stack<>();
    
    public void transform(String s) {

    }

    private boolean isNumber(char c) {
        return c >= 48 && c <= 57;
    }

    public CalculateString(String s) {
        int len = s.length();
        int i = 0;
        while (i < len) {
            char c = s.charAt(i);
            //处理数字
            double tmp = 0;
            int decimal = 0;
            boolean isDot = false;
            if (isNumber(c)) {
                tmp *= 10;
                tmp += (c - 48);
                if (isDot) {
                    decimal++;
                }
            }
            else if (c == 48) {
                isDot = true;
            }
            else {
                for (int k = 0; k < decimal; k++) {
                    tmp /= 10;
                }
                vals.push(tmp);
                isDot = false;
                decimal = 0;
                if (s.equals("+")) {
                    ops.push(s);
                }
            }
            i++;
        }
    }

    public double answer() {

        return 0;
    }
    
    public static void main(String[] args) {
        System.out.println("Input a String and press Enter to calculate:");
        String s = StdIn.readLine();
        CalculateString cal = new CalculateString(s);
        System.out.println("Answer:");
        System.out.println(cal.answer());
    }
}