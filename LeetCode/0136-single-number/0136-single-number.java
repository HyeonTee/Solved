class Solution {
    public int singleNumber(int[] nums) {
        int bits = 0;
        for (int num : nums) {
            bits = bits ^ num;
        }
        
        return bits;
    }
}