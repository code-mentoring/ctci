package gaurav;

import java.util.Arrays;

/**
 * 1.8 - Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
 * its entire row and column are set to 0.
 */
public class Solution1_8 {
    public static void main(String[] args) {
        int[][] arr1 = {{1, 2, 3},
                        {4, 5, 0, 3, 4},
                        {7, 8, 9}};
        //row,col -> (1,2) => 1st rows is Zero and 2nd column is Zero
        Arrays.stream(new Solution1_8().zeroRowColumn(arr1)).forEach(element -> {
            for (int x : element) {
                System.out.print(x + "\t");
            }
            System.out.println();
        });
    }

    public int[][] zeroRowColumn(int[][] input) {
        int tempRow = 0;
        int tempCol = 0;
        for (int rows = 0; rows < input.length; rows++) {
            for (int cols = 0; cols < input.length; cols++) {
                if (input[rows][cols] == 0) {
                    tempRow = rows;
                    tempCol = cols;
                    break;
                }
            }
        }
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length; j++) {
                input[tempRow][j] = 0;
                input[i][tempCol] = 0;
            }
        }
        return input;
    }
}
