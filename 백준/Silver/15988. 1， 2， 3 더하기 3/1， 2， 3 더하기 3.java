import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        int divider = 1_000_000_009;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        int[] nums = new int[T];
        int max = 0;
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            nums[t] = n;
            max = Math.max(max, n);
        }

        long[] dp = new long[max + 1];
        dp[1] = 1;
        if (max > 1) dp[2] = 2;
        if (max > 2) dp[3] = 4;
        for (int i = 4; i <= max; i++) {
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % divider;
        }

        for (int i = 0; i < T; i++) {
            sb.append(dp[nums[i]]).append("\n");
        }

        System.out.println(sb);
    }
}