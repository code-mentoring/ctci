package gaurav;

import java.util.Arrays;

/**
 * 1.7 - Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is an integer,
 * write a method to rotate the image by 90 degrees. Can you do this in place?
 */
public class Solution1_7 {
    public static void main(String[] args) {
        int[][] arr1 = {{1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9}};
        int[][] arr2 = {{1, 2, 3, 4},
                        {5, 6, 7, 8},
                        {9, 10, 11, 12},
                        {13, 14, 15, 16}};

        Arrays.stream(new Solution1_7().rotate90Degree(arr2)).forEach(element -> {
            for (int x : element) {
                System.out.print(x + "\t");
            }
            System.out.println();
        });
    }

    private int[][] rotate90Degree(int[][] input) {
        for (int rows = 0; rows < input.length; rows++) {
            for (int cols = rows; cols < input.length; cols++) {
                int temp = input[rows][cols];
                input[rows][cols] = input[cols][rows];
                input[cols][rows] = temp;
            }
        }
        for (int rows = 0; rows < input.length; rows++) {
            for (int cols = 0; cols < input.length / 2; cols++) {
                int temp = input[rows][cols];
                input[rows][cols] = input[rows][input.length - 1 - cols];
                input[rows][input.length - 1 - cols] = temp;
            }
        }
        return input;
    }
}
