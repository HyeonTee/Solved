import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[] nums = new int[n];

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                nums[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(nums);

            int diffMin = Integer.MAX_VALUE;
            int cnt = 0;
            int lt = 0;
            int rt = n-1;

            while (lt < rt) {
                int sum = nums[lt] + nums[rt];
                int diff = Math.abs(sum - k);
                if (diffMin > diff) {
                    diffMin = diff;
                    cnt = 1;
                } else if (diffMin == diff) {
                    cnt++;
                }

                if (sum >= k) {
                    rt--;
                } else {
                    lt++;
                }
            }

            bw.write(cnt + "\n");
        }

        bw.close();
        br.close();
    }
}