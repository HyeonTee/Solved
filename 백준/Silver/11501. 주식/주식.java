import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] stocks = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                stocks[j] = Integer.parseInt(st.nextToken());
            }

            long profit = 0;
            int max = stocks[n-1];
            for (int j = n-1; j >= 0; j--) {
                int curr = stocks[j];
                if (curr > max) {
                    max = curr;
                }

                if (curr < max) {
                    profit += (max - curr);
                }
            }

            bw.write(profit + "\n");
        }


        bw.write(  "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}