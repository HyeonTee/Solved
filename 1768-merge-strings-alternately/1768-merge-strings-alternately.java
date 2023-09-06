class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        
        String newString = "";
        if (n1 > n2) {
            for (int i =0; i < n2; i++) {
                newString += word1.charAt(i);
                newString += word2.charAt(i);
            }
            newString += word1.substring(n2, n1);
        } else {
            for (int i =0; i < n1; i++) {
                newString += word1.charAt(i);
                newString += word2.charAt(i);
            }
            newString += word2.substring(n1, n2);
        }
        
        return newString;
    }
}