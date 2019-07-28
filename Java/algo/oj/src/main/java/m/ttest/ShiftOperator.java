package m.ttest;

/**
 * ShiftOperator
 */
public class ShiftOperator {

    public static void main(String[] args) {
        int x = 32;
        int y = x >> 1;
        int z = x >>> 1;
        System.out.print("x >> 1:" + y + "\nx >>> 1:" + z);
    }
}