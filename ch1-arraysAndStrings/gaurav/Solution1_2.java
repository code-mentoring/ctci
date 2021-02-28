package gaurav;

/**
 * 1.2 - Check Permutation Given two strings, write a method to decide if one is a permutation of the other.
 */
public class Solution1_2 {
    public static void main(String[] args) {
        System.out.println(new Solution1_2().permutationOfStrings("abc", "dcef"));
        System.out.println(new Solution1_2().permutationOfStrings("abc", "bca"));
        System.out.println(new Solution1_2().permutationOfStrings("abacd", "abace"));
    }

    private boolean permutationOfStrings(String inputOne, String inputTwo) {
        boolean flag = true;
        if (!inputOne.equalsIgnoreCase(inputTwo) && inputOne.length() != inputTwo.length()) {
            return false;
        }
        for (int i = 0; i < inputOne.length(); i++) {
            if (!inputTwo.contains(Character.toString(inputOne.charAt(i)))) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}
