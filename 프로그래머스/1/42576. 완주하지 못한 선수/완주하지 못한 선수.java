import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> memo = new HashMap<>();
        
        for (String p : participant) {
            if (memo.containsKey(p)) {
                memo.put(p, memo.get(p) + 1);
            } else {
                memo.put(p, 1);
            }
        }
        
        for (String c : completion) {
            memo.put(c, memo.get(c) - 1);
        }
        
        for (String p : participant) {
            if (memo.get(p) == 1) {
                answer = p;
            }
        }
        
        return answer;
    }
}