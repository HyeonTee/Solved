class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        int minPrice = 100001;

        for (int price : prices) {
            if (price - minPrice > profit) {
                profit = price - minPrice;
            }

            if (minPrice > price) {
                minPrice = price;
            }
        }

        return profit;
    }
}