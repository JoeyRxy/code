package m.learn;

/**
 * MException
 */
public class MException extends Exception{

    public MException() {
        super("This is My Exception Test!");
    }

    public static void main(String[] args) {
        int[] a = new int[3];
        /* try {
            for (int i = 0; i < 4; i++) {
                a[i] = 1;
            }
        } catch (MException e) {
            //TODO: handle exception
        } */
    }
}