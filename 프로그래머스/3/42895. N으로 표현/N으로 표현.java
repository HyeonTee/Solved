import java.util.*;

class Solution {
    public int solution(int N, int number) {
        Map<Integer, Integer> map = new HashMap<>();
        
        int k = N;
        for (int i = 1; i <= 9; i++) {
            map.put(k, i);
            k = k * 10 + N;
        }
        
        recur(N, 0, 0, map);
        
        return map.getOrDefault(number, -1);
    }
    
    void recur(int n, int cnt, int curr, Map<Integer, Integer> map) {
        if (cnt > 8) {
            return;
        }
        
        map.put(curr, Math.min(map.getOrDefault(curr, cnt), cnt));
        
        int k = n;
        for (int i = 1; i <= 9; i++) {
            recur(n, cnt + i, curr + k, map);
            recur(n, cnt + i, curr - k, map);
            recur(n, cnt + i, curr * k, map);
            recur(n, cnt + i, curr / k, map);
            k = k * 10 + n;
        }
    }
}