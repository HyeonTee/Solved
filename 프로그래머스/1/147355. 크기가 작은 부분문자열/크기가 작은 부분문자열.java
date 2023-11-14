class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        long numP = Long.parseLong(p);
        
        for (int i = 0; i < t.length() - n + 1; i++) {
            String substr = t.substring(i, i + n);
            long subLong = Long.parseLong(substr);
            if (subLong <= numP) {
                answer++;
            }
        }
        
        return answer;
    }
}