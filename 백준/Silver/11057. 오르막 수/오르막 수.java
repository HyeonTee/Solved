import java.io.*;

public class Main {
    static final int MOD = 10007;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        long result = 1;

        for (int i = 1; i <= 9; i++) {
            result = (result * (n + i)) % MOD;
        }

        long denom = 1;
        for (int i = 1; i <= 9; i++) {
            denom = (denom * i) % MOD;
        }

        result = (result * modPow(denom, MOD - 2)) % MOD;

        System.out.println(result);
    }

    static long modPow(long a, int b) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            b >>= 1;
        }
        return res;
    }
}
