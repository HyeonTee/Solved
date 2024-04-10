import java.util.*;
import java.io.*;


public class Main {
    static int n;
    static Map<Integer, List<Integer>> edges;
    static boolean[] visited;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edges.put(i, new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                if (st.nextToken().equals("1")) {
                    edges.get(i).add(j);
                }
            }
        }

        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            visited = new boolean[n];
            dfs(i);
            for (int j = 0; j < n; j++) {
                if (visited[j]) {
                    matrix[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bw.write(matrix[i][j] + " ");
            }
            bw.write('\n');
        }

        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int v) {
        for (int w : edges.get(v)) {
            if (!visited[w]) {
                visited[w] = true;
                dfs(w);
            }
        }
    }
}