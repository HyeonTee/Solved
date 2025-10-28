import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n+1];
        for (int i = n-1; 0 <= i; i--) {
            int days = arr[i][0];
            int pay = arr[i][1];

            if (i + days > n) {
                dp[i] = dp[i+1];
            } else {
                dp[i] = max(dp[i+1], dp[i+days] + pay);
            }
        }

        System.out.println(dp[0]);
    }

    static int max(int a, int b) {
        return a > b ? a : b;
    }
}