import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int num : nums) {
            int count = countMap.getOrDefault(num, 0) + 1;
            if (count > nums.length / 2) {
                return num;
            }
            countMap.put(num, count);
        }

        return -1;
    }
}