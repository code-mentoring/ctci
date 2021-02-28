
/**
 * 1.1 - Is Unique Implement an algorithm to determine if a string has all unique characters.
 * What if you cannot use additional data structures?
 */
package gaurav;

public class Solution1_1 {
    public static void main(String[] args) {
        System.out.println(new Solution1_1().uniqueAlgo("abcd"));
    }

    private boolean uniqueAlgo(String input) {
        for (int i = 0, j = input.length() - 1; i < input.length() && j >= 0; i++, j--) {
            if (input.charAt(i) == input.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
