package m.learn;

import java.util.Random;

/**
 * CountingSort
 */
public class CountingSort {
    private int[] count;
    private int[] x;

    public CountingSort(int[] a) {
        //duplicate
        int len = a.length;
        x = new int[len];
        for (int i = 0; i < len; i++) {
            x[i] = a[i];
        }
        int max = x[0], min = x[0];
        for (int i = 1; i < len; i++) {
            if (max < x[i])
                max = x[i];
            if (min > x[i])
                min = x[i];
        }
        //将数组整体偏移，使最小值为0
        for (int i = 0; i < len; i++) {
            x[i] -= min;
        }
        //计数
        int size = max - min + 1;
        count = new int[size];
        for (int i = 0; i < len; i++) {
            count[x[i]]++;
        }
        //sorting
        int index = 0;//index for sorted array
        for (int i = 0; i < size; i++) {
            while (count[i] > 0) {
                x[index] = i;
                count[i]--;
                index++;
            }
        }
        //还原偏移
        for (int i = 0; i < len; i++) {
            x[i] += min;
        }
    }
    
    public void print() {
        for (int i = 0; i < x.length; i++) {
            System.out.println(x[i]);
        }
    }
    public static void main(String[] args) {
        int[] x = new int[100];
        Random r = new Random();
        for (int i = 0; i < x.length; i++) {
            x[i] = r.nextInt() % 1000;
        }
        CountingSort o = new CountingSort(x);
        o.print();
    }
}