import java.io.*;

public class Main {
    static boolean isSquare(int x) {
        int r = (int) Math.sqrt(x);
        return r * r == x;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (isSquare(n)) {
            System.out.println(1);
            return;
        }

        for (int i = 1; i * i <= n; i++) {
            if (isSquare(n - i * i)) {
                System.out.println(2);
                return;
            }
        }

        int m = n;
        while (m % 4 == 0) m /= 4;
        if (m % 8 == 7) {
            System.out.println(4);
        } else {
            System.out.println(3);
        }
    }
}