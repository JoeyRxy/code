package m.ttest;

/**
 * test2
 */
public class test2 {

    /**
     * Do
     */
    public interface Do {

        int Add(int x, int y);

        int Multi(int x, int y);
    }

    /**
     * Hello
     */
    public class Hello implements Do {

        @Override
        public int Add(int x, int y) {
            return x + y;
        }

        @Override
        public int Multi(int x, int y) {
            return x * y;
        }

    }

    public void test(Do it) {
        int[] x = { 1, 2, 3, 4 };
        int[] y = { 9, 8, 7, 6 };
        for (int i = 0; i < 4; i++) {
            int ans = it.Add(x[i], y[i]);
            System.out.println(ans);
        }
    }

    public static void main(String[] args) {
        test2 t = new test2();
        t.test(t.new Hello());
    }
}