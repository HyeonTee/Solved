class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if ((str1 + str2).equals(str2 + str1) == false) {
            return "";
        }
        
        int len1 = str1.length();
        int len2 = str2.length();
        int len_gcd = gcd(len1, len2);
        
        return str1.substring(0, len_gcd);
        
    }
    
    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        
        return gcd(b, a % b);
    }
}