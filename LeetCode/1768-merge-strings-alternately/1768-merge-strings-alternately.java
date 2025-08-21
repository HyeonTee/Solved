import java.util.*;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int len1 = word1.length();
        int len2 = word2.length();
        
        if (len1 > len2) {
            for (int i = 0; i < len2; i++) {
                sb.append(word1.charAt(i));
                sb.append(word2.charAt(i));
            }
            sb.append(word1.substring(len2));
        } else {
            for (int i = 0; i < len1; i++) {
                sb.append(word1.charAt(i));
                sb.append(word2.charAt(i));
            }
            sb.append(word2.substring(len1));
        }

        return sb.toString();        
    }
}