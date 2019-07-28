package m.matrix;

/**
 * Matrix
 */
public class Matrix {

    private double[][] matrix;
    /**
     * 
     * @param n raw
     * @param m column
     */
    public Matrix(int n,int m) {
        matrix = new double[n][m];
        for (int i = 0; i < n; i++) {
            matrix[i] = new double[m];
        }
    }
}