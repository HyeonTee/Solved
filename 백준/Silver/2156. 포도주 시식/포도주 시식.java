import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] wines = new int[n];
        for (int i = 0; i < n; i++) {
            wines[i] = Integer.parseInt(br.readLine());
        }

        if (n == 1) {
            System.out.println(wines[0]);
            return;
        }

        if (n == 2) {
            System.out.println(wines[0] + wines[1]);
            return;
        }

        int[][] dp = new int[n][2];
        dp[0][0] = 0;
        dp[0][1] = wines[0];
        dp[1][0] = wines[0];
        dp[1][1] = wines[0] + wines[1];

        for (int i = 2; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = Math.max(dp[i - 2][0] + wines[i - 1] + wines[i], dp[i-1][0] + wines[i]);
        }

        System.out.println(Math.max(dp[n - 1][1], dp[n - 1][0]));
    }
}