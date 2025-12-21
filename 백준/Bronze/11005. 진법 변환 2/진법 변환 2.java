import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        if (n == 0) {
            System.out.println(0);
            return;
        }

        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            int remainder = n % b;

            if (remainder < 10) sb.append((char)('0' + remainder));
            else sb.append((char)('A' + (remainder - 10)));

            n /= b;
        }

        System.out.println(sb.reverse());
    }
}