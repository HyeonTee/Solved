class Solution {
    public int maxArea(int[] height) {
        int lt = 0;
        int rt = height.length - 1;
        int max = 0;

        while (lt < rt) {
            max = max(min(height[lt], height[rt]) * (rt - lt), max);
            if (height[lt] > height[rt]) {
                rt--;
            }
            else {
                lt++;
            }
        }

        return max;
    }

    static int max(int a, int b) {
        return a > b ? a : b;
    }

    static int min(int a, int b) {
        return a > b ? b : a;
    }
}