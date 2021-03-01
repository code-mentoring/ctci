/**
 * @author [Mohamad Jayyusi]
 * @email
 * @create date 2021-02-23
 * @modify date 2021-02-23
 * @desc 1.8 - Zero Matrix: Write an algorithm such that if an element in an MxN
 *       matrix is 0, its entire row and column are set to 0.
 */

public class mohamad_jayyusi__1_8 {

    private static final int m = 8;
    private static final int n = 8;
    private static int[][] matrix = new int[m][n];
    // O(n²) a multi dimension array to store the indices where there is a
    // zero in the original matrix
    private static int[][] zeroIndices = new int[m][n];

    public static void main(String[] args) {

        initializeMatrix();
        setZero(0, 0);
        printMatrix();
        // O(n²) additional space
        findZeroIndices();
        zeroMatrix();
        System.out.println();
        printMatrix();
    }

    // O(n²) additional space - O(n²) time complexity
    public static void findZeroIndices() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0)
                    zeroIndices[i][j] = 0;
            }
        }
    }

    // O(n²) time complexity
    public static void zeroMatrix() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (zeroIndices[i][j] == 0)
                    setRowAndColToZeros(i, j);
            }
        }
    }

    public static void setZero(int m, int n) {
        matrix[m][n] = 0;
    }

    // O(n)
    public static void setRowAndColToZeros(int rowNum, int ColNum) {
        for (int j = 0; j < n; j++) {
            setZero(rowNum, j);
        }
        for (int i = 0; i < m; i++) {
            setZero(i, ColNum);
        }
    }

    public static void initializeMatrix() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = 9;
                zeroIndices[i][j] = 1;
            }
        }
    }

    public static void printMatrix() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.println();
        }
    }
}
