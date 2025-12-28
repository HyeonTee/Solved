import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());

            int[][] scores = new int[2][n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                scores[0][i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                scores[1][i] = Integer.parseInt(st.nextToken());
            }

            if (n == 1) {
                sb.append(Math.max(scores[0][0], scores[1][0])).append('\n');
                continue;
            }

            int[][] dp = new int[2][n];
            dp[0][0] = scores[0][0];
            dp[1][0] = scores[1][0];
            dp[0][1] = scores[1][0] + scores[0][1];
            dp[1][1] = scores[0][0] + scores[1][1];

            for (int i = 2; i < n; i++) {
                dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + scores[0][i];
                dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + scores[1][i];
            }

            sb.append(Math.max(dp[0][n-1], dp[1][n-1])).append('\n');
        }

        System.out.println(sb);
    }
}