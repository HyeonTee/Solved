class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        
        for (int i = 0; i <= n; i++) {
            int cnt = countOnes(i);
            ans[i] = cnt;
        }
        
        return ans;
    }
    
    static int countOnes(int x) {
        int cnt = 0;
        
        while (x != 0) {
            x = x & (x - 1);
            cnt++;
        }
        
        return cnt;
    }
}