import java.io.*;
import java.util.*;

public class Main {
    static int result = 0;
    static Map<Integer, ArrayList<Integer>> map;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.get(a).add(b);
            map.get(b).add(a);
        }

        for (int i = 0; i < n; i++) {
            visited = new boolean[n];
            dfs(i, 1);
            if (result == 1) break;
        }

        System.out.println(result);
    }

    static void dfs(int v, int length) {
        if (result == 1) return;
        if (length == 5) {
            result = 1;
            return;
        }

        visited[v] = true;
        for (int w : map.get(v)) {
            if (!visited[w]) {
                dfs(w, length + 1);
            }
        }
        visited[v] = false;
    }
}