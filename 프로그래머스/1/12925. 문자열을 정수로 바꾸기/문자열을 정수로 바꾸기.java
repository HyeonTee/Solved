class Solution {
    public int solution(String s) {
        int n = s.length();
        int answer = 0;
        
        for (int i = n-1; i > 0; i--) {
            int tmp = s.charAt(i) - '0';
            answer += tmp * Math.pow(10, n-i-1);
        }
        
        if (s.charAt(0) == '-') {
            answer *= -1;
        } else if (s.charAt(0) == '+') {
        } else {
            answer += (s.charAt(0) - '0') * Math.pow(10, n-1);
        }
        return answer;
    }
}