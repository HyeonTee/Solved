import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1_000_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        int[][] cost = new int[n][3];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            cost[i][0] = Integer.parseInt(st.nextToken()); // R
            cost[i][1] = Integer.parseInt(st.nextToken()); // G
            cost[i][2] = Integer.parseInt(st.nextToken()); // B
        }

        int answer = getAnswer(cost, n);

        System.out.println(answer);
    }

    static int getAnswer(int[][] cost, int n) {
        int answer = INF;

        for (int first = 0; first < 3; first++) {
            int r = INF, g = INF, b = INF;

            if (first == 0) r = cost[0][0];
            if (first == 1) g = cost[0][1];
            if (first == 2) b = cost[0][2];

            for (int i = 1; i < n; i++) {
                int nr = cost[i][0] + Math.min(g, b);
                int ng = cost[i][1] + Math.min(r, b);
                int nb = cost[i][2] + Math.min(r, g);

                r = nr;
                g = ng;
                b = nb;
            }

            if (first == 0) answer = Math.min(answer, Math.min(g, b));
            if (first == 1) answer = Math.min(answer, Math.min(r, b));
            if (first == 2) answer = Math.min(answer, Math.min(r, g));
        }
        return answer;
    }
}