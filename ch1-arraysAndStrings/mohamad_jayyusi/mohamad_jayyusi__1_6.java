
/**
 * @author [Mohamad Jayyusi]
 * @email 
 * @create date 2021-02-23
 * @modify date 2021-02-23
 * @desc 1.6 - String Compression: Implement a method to perform basic string compression using 
 * the counts of repeated characters. For example, the string a a b c c c c c a a a would become 
 * a 2 b 1 c 5 a 3 , If the "compressed" string would not become smaller than the original string, 
 * your method should return the original string. You can assume the string has only uppercase 
 * and lowercase letters (a - z). */

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class mohamad_jayyusi__1_6 {

    public static String compress(String str) {
        String result = "";
        int i = 0, j;
        while (i < str.length()) {
            int count = 1;
            for (j = i + 1; j < str.length() && (str.charAt(i) == str.charAt(j)); j++) {
                count++;
            }
            result = result + str.charAt(i) + count;
            i += count;
        }
        return result.length() < str.length() ? result : str;

    }

    @Test
    public void testStringCompression() {
        assertEquals("a2b1c5a3", compress("aabcccccaaa"));
        assertEquals("abc", compress("abc"));// a1b1c1
        assertEquals("aabc", compress("aabc"));// a2b1c1
        assertEquals("bc", compress("bc"));// b1c1
        assertEquals("a", compress("a"));// a1
        assertEquals("a4", compress("aaaa"));
        assertEquals("a5c1", compress("aaaaac"));
        assertEquals("aba", compress("aba"));// a1b1a1
        assertEquals("abcc", compress("abcc"));// a1b1c2
    }
}