import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static Map<Integer, List<Integer>> edges;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        String input;
        StringTokenizer st;

        edges = new HashMap<>();
        for (int i = 1; i < n+1; i++) {
            edges.put(i, new ArrayList<>());
        }

        while (!(input = br.readLine()).equals("-1 -1")) {
            st = new StringTokenizer(input);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            edges.get(a).add(b);
            edges.get(b).add(a);
        }

        int[] scores = new int[n+1];
        int min = Integer.MAX_VALUE;
        for (int i = 1; i < n+1; i++) {
            int score = bfs(i);
            scores[i] = score;
            if (score < min) {
                min = score;
            }
        }

        int cnt = 0;
        StringBuilder candidates = new StringBuilder();
        for (int i = 1; i < n+1; i++) {
            if (scores[i] == min) {
                cnt++;
                candidates.append(i + " ");
            }
        }

        bw.write(min + " " + cnt + "\n");
        bw.write(candidates.toString());

        bw.flush();
        bw.close();
        br.close();
    }

    static int bfs(int start) {
        boolean[] visited = new boolean[n+1];
        int[] dist = new int[n+1];

        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        while (!q.isEmpty()) {
            int v = q.poll();
            for (int w : edges.get(v)) {
                if (!visited[w]) {
                    visited[w] = true;
                    dist[w] = dist[v] + 1;
                    q.offer(w);
                }
            }
        }

        dist[start] = 0;

        int max = 0;
        for (int i = 1; i < n+1; i++) {
            if (dist[i] > max) {
                max = dist[i];
            }
        }

        return max;
    }
}
