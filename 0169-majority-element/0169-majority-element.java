import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);

        int ans = nums[0];
        int cnt = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                cnt++;
                if (cnt > nums.length >> 1) {
                    ans = nums[i];
                    break;
                }
            } else {
                cnt = 1;
            }
        }

        return ans;
    }
}