import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    static boolean[] visited;
    static int n, m;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        visited = new boolean[n];

        dfs(0);
        System.out.println(sb);
    }

    static void dfs(int length) {
        if (length == m) {
            for (int i = 0; i < m; i++) {
                sb.append(arr[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (length > 0) {
                    if (arr[length - 1] < i+1) {
                        visited[i] = true;
                        arr[length] = i+1;
                        dfs(length + 1);
                        visited[i] = false;
                    }
                } else {
                    visited[i] = true;
                    arr[length] = i+1;
                    dfs(length + 1);
                    visited[i] = false;
                }
            }
        }
    }
}