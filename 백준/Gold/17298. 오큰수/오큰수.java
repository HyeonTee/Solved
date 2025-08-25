import java.io.*;
import java.util.*;

public class Main {
    static final class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        FastScanner(InputStream is) { this.in = is; }
        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
        int nextInt() throws IOException {
            int c, sgn = 1, x = 0;
            do c = read(); while (c <= ' ');
            if (c == '-') { sgn = -1; c = read(); }
            while (c > ' ') { x = x * 10 + (c - '0'); c = read(); }
            return x * sgn;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        int n = fs.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = fs.nextInt();

        int[] result = new int[n];
        Arrays.fill(result, -1);

        int[] stack = new int[n];
        int top = -1;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            while (top >= 0 && num > nums[stack[top]]) {
                result[stack[top--]] = num;
            }
            stack[++top] = i;
        }

        StringBuilder sb = new StringBuilder(n * 3);
        for (int i = 0; i < n; i++) {
            sb.append(result[i]);
            if (i + 1 < n) sb.append(' ');
        }
        System.out.print(sb);
    }
}