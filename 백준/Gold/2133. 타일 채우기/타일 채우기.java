import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        if (n % 2 == 1) {
            System.out.println(0);
            return;
        }

        long[] dp = new long[n + 1];
        dp[0] = 1;
        if (n >= 2) dp[2] = 3;

        long acc = 0;
        for (int i = 4; i <= n; i += 2) {
            acc += dp[i - 4];
            dp[i] = 3 * dp[i - 2] + 2 * acc;
        }

        System.out.println(dp[n]);
    }
}
