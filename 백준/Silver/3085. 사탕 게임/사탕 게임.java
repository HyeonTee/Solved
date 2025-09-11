import java.io.*;

public class Main {
    static char[][] board;
    static int max = 1;
    static int n;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-1; j++) {
                if (board[i][j] != board[i][j+1]) {
                    swapAndCalMax(i, j, i, j+1);
                }
            }
        }

        for (int i = 0; i < n-1; i++) {
            for  (int j = 0; j < n; j++) {
                if (board[i][j] != board[i+1][j]) {
                    swapAndCalMax(i, j, i+1, j);
                }
            }
        }

        System.out.println(max);
    }

    static void calMax() {
        for (int i = 0; i < n; i++) {
            int curr = 1;
            for (int j = 0; j < n-1; j++) {
                if (board[i][j] == board[i][j+1]) {
                    curr++;
                    max = Math.max(max, curr);
                } else {
                    curr = 1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            int curr = 1;
            for (int j = 0; j < n-1; j++) {
                if (board[j][i] == board[j+1][i]) {
                    curr++;
                    max = Math.max(max, curr);
                } else {
                    curr = 1;
                }
            }
        }
    }

    static void swapAndCalMax(int x, int y, int i, int j) {
        char temp = board[x][y];
        board[x][y] = board[i][j];
        board[i][j] = temp;
        calMax();
        board[i][j] = board[x][y];
        board[x][y] = temp;
    }
}
