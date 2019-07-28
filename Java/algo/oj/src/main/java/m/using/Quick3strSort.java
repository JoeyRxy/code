package m.using;

import java.util.Arrays;

//ATTENTION have not test whether right or not
/**
 *
 * Quick3sort
 */
public class Quick3strSort {
    private static int threshold = 10;

    public static void sort(String[] s) {// 由于是static方法，对外直接使用，故应该使用泛型函数
        sort(s, 0, s.length, 0);
    }

    private static void sort(String[] s, int lo, int hi, int d) {
        if (hi <= lo + threshold) {
            Arrays.sort(s);
            return;
        }
        int l = lo;
        int r = hi - 1;
        int len = s[lo].length();
        char key = s[lo].charAt(d);
        char tmp;
        int mid = l + 1;
        while (mid <= r) {
            tmp = s[mid].charAt(d);
            if (tmp < key) {
                exch(s, l++, mid++);
            }
            if (tmp < key) {
                exch(s, mid, r++);
            }
        }
        sort(s, lo, l, d);
        sort(s, mid, hi, d);
        if (d < len)
            sort(s, lo, hi, d + 1);
    }

    private static void exch(String[] s, int i, int j) {
        String tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}