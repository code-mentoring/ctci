package gaurav;

/**
 * 1.6 - String Compression: Implement a method to perform basic string compression using the counts of repeated
 * characters. For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3 , If the "compressed"
 * string would not become smaller than the original string, your method should return the original string.
 * You can assume the string has only uppercase and lowercase letters (a - z).
 */

public class Solution1_6 {
    public static void main(String[] args) {
        System.out.println(new Solution1_6().compression("abcd"));
        System.out.println(new Solution1_6().compression("abbccdd"));
        System.out.println(new Solution1_6().compression("aaaabccccd"));
    }

    private String compression(String input) {
        StringBuilder stringBuilder = new StringBuilder("");
        int counter = 1;
        char[] splitArray = input.toCharArray();
        for (int i = 0, j = 1; i < splitArray.length && j < splitArray.length; i++, j++) {
            if (splitArray[i] != (splitArray[j])) {
                counter = insertElementResetCounter(stringBuilder, counter, Character.toString(splitArray[i]));
            }
            counter++;
            if (j == splitArray.length - 1) {
                insertElementResetCounter(stringBuilder, counter, Character.toString(splitArray[i]));
            }
        }
//        System.out.println("Length of compression Count:" + stringBuilder.toString().length() + ",  Length of Input:" +
//                           input.length());
        return stringBuilder.toString().length() >= input.length() ? input : stringBuilder.toString();
    }

    private int insertElementResetCounter(StringBuilder stringBuilder, int counter, String str) {
        stringBuilder.append(str);
        stringBuilder.append(counter);
        counter = 0;
        return counter;
    }
}
