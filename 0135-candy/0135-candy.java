class Solution {
    public int candy(int[] ratings) {
        int result = 0;

        int[] candies = new int[ratings.length];
        candies[0] = 1;

        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i - 1] < ratings[i]) {
                candies[i] = candies[i - 1] + 1;
            } else {
                candies[i] = 1;
            }
        }

        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = max(candies[i + 1] + 1, candies[i]);
            }
        }

        for (int candy : candies) {
            result += candy;
        }

        return result;
    }

    int max(int a, int b) {
        return a > b ? a : b;
    }
}