import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] c = new int[m];
        for (int i = 0; i < m; i++) c[i] = i + 1;

        StringBuilder sb = new StringBuilder();
        while (true) {
            for (int x : c) sb.append(x).append(' ');
            sb.append('\n');

            int i = m - 1;
            while (i >= 0 && c[i] == n - (m - 1 - i)) i--;
            if (i < 0) break;

            c[i]++;
            for (int j = i + 1; j < m; j++) c[j] = c[j - 1] + 1;
        }

        System.out.print(sb);
    }
}