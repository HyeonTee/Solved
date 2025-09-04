import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] tail = new int[n];
        int len = 0;
        for (int x : arr) {
            int pos = Arrays.binarySearch(tail, 0, len, x);
            if (pos < 0) pos = -pos - 1;
            tail[pos] = x;
            if (pos == len) len++;
        }
        System.out.println(len);
    }
}