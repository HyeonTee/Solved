import java.util.*;
import java.io.*;

class Solution {
    public String reverseWords(String s) {
        StringTokenizer st = new StringTokenizer(s);
        StringBuilder sb = new StringBuilder();
        
        int n = st.countTokens();
        String[] tokens = new String[n];
        for (int i = 0; i < n; i++) {
            tokens[n - i - 1] = st.nextToken();
        }
        
        for (int i = 0; i < n - 1; i++) {
            sb.append(tokens[i]);
            sb.append(" ");
        }
        
        sb.append(tokens[n-1]);
        
        return sb.toString();
    }
}