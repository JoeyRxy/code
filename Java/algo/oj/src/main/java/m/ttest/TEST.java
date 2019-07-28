package m.ttest;

/**
 * TEST
 */
public class TEST {
    // private boolean[][] table;

    public static void main(String[] args) {
        // is local variable initialize automatelly
        boolean[][] table = new boolean[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(table[i][j] + "\t");
            }
            System.out.println();
        }

        // ===========//
        // char[] to String?
        char[] c = { 'h', 'e', 'l', 'l', 'o' };
        String s = new String(c);
        System.out.print(s);
        // =============//
        // String.valueOf()
        int N = 100;
        String valueOf = String.valueOf(N);
        System.out.println(valueOf);
    }
}