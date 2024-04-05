import java.util.*;
import java.io.*;

class IceBerg {
    int x;
    int y;

    IceBerg(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[] dx = {1, -1, 0, 0 };
    static int[] dy = {0, 0, 1, -1 };

    static int n, m;
    static int[][] graph;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        int cnt;

        while ((cnt = SeparateNum()) < 2) {
            if (cnt == 0) {
                ans = 0;
                break;
            }

            Melt();
            ans++;
        }

        bw.write(ans + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    public static int SeparateNum() {
        boolean[][] visited = new boolean[n][m];

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != 0 && !visited[i][j]) {
                    DFS(i, j, visited);
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public static void DFS(int x, int y, boolean[][] visited) {
        visited[x][y] = true;

        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }

            if (graph[nx][ny] != 0 && !visited[nx][ny]) {
                DFS(nx, ny, visited);
            }
        }
    }
    
    public static void Melt() {
        Queue<IceBerg> queue = new LinkedList<>();

        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != 0) {
                    queue.offer(new IceBerg(i, j));
                    visited[i][j] = true;
                }
            }
        }

        int nx, ny;
        while (!queue.isEmpty()) {
            IceBerg ice = queue.poll();

            int seaNum = 0;

            for (int i = 0; i < 4; i++) {
                nx = ice.x + dx[i];
                ny = ice.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }

                if (!visited[nx][ny] && graph[nx][ny] == 0) {
                    seaNum++;
                }
            }

            if (graph[ice.x][ice.y] - seaNum < 0) {
                graph[ice.x][ice.y] = 0;
            } else {
                graph[ice.x][ice.y] -= seaNum;
            }
        }
    }
}
