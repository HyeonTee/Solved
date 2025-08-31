import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+1];
        dp[n] = 0;
        for (int i = n - 1; i > 0; i--) {
            if (i * 3 <= n) {
                dp[i] = min(dp[i + 1], dp[i * 2], dp[i * 3]) + 1;
            } else if (i * 2 <= n) {
                dp[i] = Math.min(dp[i + 1], dp[i * 2]) + 1;
            } else {
                dp[i] = dp[i + 1] + 1;
            }
        }

        System.out.println(dp[1]);
    }

    static int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}