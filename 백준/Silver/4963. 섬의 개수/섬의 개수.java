import java.io.*;
import java.util.*;

public class Main {
    static int[][] matrix;
    static boolean[][] visited;
    static int w;
    static int h;
    static final int[] dx = {1, 1, 0, -1, -1, -1, 0, 1};
    static final int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0) {
                break;
            }

            matrix = new int[h][w];
            visited = new boolean[h][w];
            for (int r = 0; r < h; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < w; c++) {
                    matrix[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            int result = 0;
            for (int r = 0; r < h; r++) {
                for (int c = 0; c < w; c++) {
                    if (!visited[r][c] && matrix[r][c] == 1) {
                        result++;
                        bfs(r, c);
                    }
                }
            }

            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }

    static void bfs(int sr, int sc) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        visited[sr][sc] = true;
        q.offer(new int[]{sr, sc});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];

            for (int dir = 0; dir < 8; dir++) {
                int nr = r + dy[dir], nc = c + dx[dir];
                if (0 <= nr && nr < h && 0 <= nc && nc < w && matrix[nr][nc] == 1 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }
        }
    }
}