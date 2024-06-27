class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                res += 1;
            } else if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
                res -= 1;
            }
        }
        
        if (res == 0) {
            return true;
        } else {
            return false;
        }
    }
}