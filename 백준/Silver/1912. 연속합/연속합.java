import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int curr = Integer.parseInt(st.nextToken());
        int best = curr;

        for (int i = 1; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            curr = Math.max(x, curr + x);
            best = Math.max(best, curr);
        }

        System.out.println(best);
    }
}