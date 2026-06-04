class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if (nums.length == 1) {
            return nums[0] >= target ? 1 : 0;
        }

        if (nums[0] >= target) {
            return 1;
        }

        int answer = nums.length + 1;
        int lt = 0;
        int rt = 1;
        int sum = nums[0] + nums[1];
        
        while (lt < rt) {
            if (nums[rt] >= target) {
                return 1;
            }

            if (sum >= target) {
                answer = Math.min(answer, rt - lt + 1);
            }

            if (rt < nums.length - 1 && (sum < target || rt == lt + 1)) {
                rt++;
                sum += nums[rt];
            } else {
                sum -= nums[lt];
                lt++;
            }
        }

        if (answer == nums.length + 1) {
            return 0;
        }

        return answer;
    }
}