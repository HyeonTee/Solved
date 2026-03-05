class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        boolean isTwice = true;
        if (nums.length == 1) {
            return 1;
        }

        int curr = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (curr == nums[i]) {
                if (isTwice) {
                    nums[k++] = nums[i];
                    isTwice = false;
                }
            } else {
                nums[k++] = nums[i];
                curr = nums[i];
                isTwice = true;
            }
        }

        return k;
    }
}