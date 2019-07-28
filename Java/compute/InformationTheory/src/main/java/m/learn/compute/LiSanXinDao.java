package m.learn.compute;

/**
 * Hello world!
 *
 */
public class LiSanXinDao 
{

    public static double log2(double x) {
        return Math.log(x)/Math.log(2);
    }

    public static double selfH(double[] Px) {
        double sum = 0;
        for (int i = 0; i < Px.length; i++) {
            sum += Px[i] * log2(Px[i]);
        }
        return sum;
    }

    public static double H(double[] Px,double[] P) {
        return 0;
    }
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
