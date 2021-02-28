package gaurav;

/**
 * 1.4 - Palindrome Permutation Given a string, write a function to check if it is a permutation of a palindrome.
 * A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
 * The palindrome does not need to be limited to just dictionary words.
 */
public class Solution1_4 {
    public static void main(String[] args) {
        System.out.println(new Solution1_4().palindromePermutation("91019"));
        System.out.println(new Solution1_4().palindromePermutation("KAYAK"));
        System.out.println(new Solution1_4().palindromePermutation("TACO CAT"));
        System.out.println(new Solution1_4().palindromePermutation("SOLOS"));
    }

    private boolean palindromePermutation(String input) {
        boolean flag = false;
        for (int i = 0, j = input.length() - 1; i < input.length() & j >= 0; i++, j--) {
            if (input.charAt(i) == input.charAt(j)) {
                flag = true;
            } else {
                flag = false;
                break;
            }
        }
        return flag;
    }
}
