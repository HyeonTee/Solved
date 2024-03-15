import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] dpMin = new int[3];
        int[] dpMax = new int[3];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 3; i++) {
            dpMin[i] = dpMax[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int num0 = Integer.parseInt(st.nextToken());
            int num1 = Integer.parseInt(st.nextToken());
            int num2 = Integer.parseInt(st.nextToken());

            int beforeMax0 = dpMax[0];
            int beforeMax1 = dpMax[1];
            int beforeMax2 = dpMax[2];

            dpMax[0] = num0 + max(beforeMax0, beforeMax1);
            dpMax[1] = num1 + max(beforeMax0, beforeMax1, beforeMax2);
            dpMax[2] = num2 + max(beforeMax1, beforeMax2);

            int beforeMin0 = dpMin[0];
            int beforeMin1 = dpMin[1];
            int beforeMin2 = dpMin[2];

            dpMin[0] = num0 + min(beforeMin0, beforeMin1);
            dpMin[1] = num1 + min(beforeMin0, beforeMin1, beforeMin2);
            dpMin[2] = num2 + min(beforeMin1, beforeMin2);
        }

        bw.write(max(dpMax[0], dpMax[1], dpMax[2]) + " ");
        bw.write(min(dpMin[0], dpMin[1], dpMin[2]) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    static int max(int a, int b, int c) {
        int ab = (a > b) ? a : b;
        return (ab > c) ? ab : c;
    }

    static int min(int a, int b) {
        return (a < b) ? a : b;
    }

    static int min(int a, int b, int c) {
        int ab = (a < b) ? a : b;
        return (ab < c) ? ab : c;
    }
}
