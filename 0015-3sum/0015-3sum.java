import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            if (nums[i] > 0) {
                break;
            }

            int lt = i + 1;
            int rt = nums.length - 1;

            while (lt < rt) {
                int sum = nums[i] + nums[lt] + nums[rt];

                if (sum < 0) {
                    lt++;
                } else if (sum > 0) {
                    rt--;
                } else {
                    answer.add(Arrays.asList(nums[i], nums[lt], nums[rt]));
                    lt++;
                    rt--;

                    while (lt < rt && nums[lt] == nums[lt - 1]) {
                        lt++;
                    }

                    while (lt < rt && nums[rt] == nums[rt + 1]) {
                        rt--;
                    }
                }
            }
        }

        return answer;
    }
}