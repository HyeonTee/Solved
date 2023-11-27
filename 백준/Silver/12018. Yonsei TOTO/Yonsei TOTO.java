import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int [] candidates = new int [n];
        int cnt = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            if (p < l) {
                candidates[cnt] = 1;
                cnt++;
            } else {
                Integer [] mileages = new Integer[p];
                for (int j = 0; j < p; j++) {
                    mileages[j] = Integer.parseInt(st.nextToken());
                }
                Arrays.sort(mileages, Collections.reverseOrder());
                candidates[cnt] = mileages[l-1];
                cnt++;
            }
        }
        
        Arrays.sort(candidates);
        for (int i = 0; i < n; i++) {
            if (candidates[i] <= m) {
                m -= candidates[i];
                ans += 1;
            } else {
                break;
            }
        }

        System.out.println(ans);
    }
}