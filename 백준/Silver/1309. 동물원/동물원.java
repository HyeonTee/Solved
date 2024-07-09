import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 3;
        for (int i = 2; i < n+1; i++) {
            dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901;
        }

        bw.write(dp[n] + "\n");

        bw.close();
        br.close();
    }
}