import java.io.*;
import java.util.*;
import java.math.*;

class Pair {
    int x, y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int n, l, r;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] states;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        states = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                states[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        while (true) {
            boolean isMoved = false;
            visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j]) {
                        visited[i][j] = true;
                        List<Pair> united = bfs(i, j);
                        if (united.size() > 1) {
                            isMoved = true;
                            int unitedSum = 0;
                            for (Pair pair : united) {
                                unitedSum += states[pair.x][pair.y];
                            }
                            int unitedAvg = unitedSum / united.size();
                            for (Pair pair : united) {
                                states[pair.x][pair.y] = unitedAvg;
                            }
                        }
                    }
                }
            }
            if (!isMoved) {
                break;
            }
            ans++;
        }
        
        bw.write(ans + "\n");
        bw.flush();

        bw.close();
        br.close();
    }

    static List<Pair> bfs(int a, int b) {
        List<Pair> temp = new ArrayList<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(a, b));
        temp.add(new Pair(a, b));
        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                    if (l <= Math.abs(states[nx][ny] - states[current.x][current.y]) && Math.abs(states[nx][ny] - states[current.x][current.y]) <= r) {
                        visited[nx][ny] = true;
                        queue.add(new Pair(nx, ny));
                        temp.add(new Pair(nx, ny));
                    }
                }
            }
        }
        return temp;
    }
}