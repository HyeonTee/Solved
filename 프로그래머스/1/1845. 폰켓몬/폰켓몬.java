import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        
        Set<Integer> uniqueNums = new HashSet<>();
        for (int num : nums) {
            uniqueNums.add(num);
        }
        
        int k = uniqueNums.size();
        
        if (n / 2 <= k) {
            return n / 2;
        }

        return k;
    }
}