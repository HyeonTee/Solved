class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int lt = m - 1;
        int rt = n - 1;
        int pt = m + n - 1;

        while (rt >= 0) {
            if (lt >= 0 && nums1[lt] > nums2[rt]) {
                nums1[pt] = nums1[lt];
                lt--;
            } else {
                nums1[pt] = nums2[rt];
                rt--;
            }
            pt--;
        }
    }
}