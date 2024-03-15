import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String X = sc.nextLine();
        String Y = sc.nextLine();

        int n = X.length();
        int m = Y.length();

        X = 'x' + X;
        Y = 'y' + Y;

        int[][] dpTable = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (X.charAt(i) == Y.charAt(j)) {
                    dpTable[i][j] = dpTable[i - 1][j - 1] + 1;
                } else {
                    dpTable[i][j] = Math.max(dpTable[i][j - 1], dpTable[i - 1][j]);
                }
            }
        }

        System.out.println(dpTable[n][m]);

        sc.close();
    }
}
