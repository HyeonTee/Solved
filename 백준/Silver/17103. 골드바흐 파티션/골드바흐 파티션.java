import java.io.*;
import java.util.Arrays;

public class Main {
    static final int MAX = 1_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] prime = new boolean[MAX + 1];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for (int i = 2; i * i <= MAX; i++) {
            if (prime[i]) {
                for (int j = i * i; j <= MAX; j += i) {
                    prime[j] = false;
                }
            }
        }

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int cnt = 0;
            
            if (n >= 4 && prime[2] && prime[n - 2]) cnt++;
            for (int a = 3; a <= n / 2; a += 2) {
                if (prime[a] && prime[n - a]) cnt++;
            }
            sb.append(cnt).append('\n');
        }

        System.out.print(sb);
    }
}

