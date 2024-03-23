import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] nm = br.readLine().split(" ");

        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        int[] data = new int[n];
        
        int lt = 0; // lt의 최솟값: data중 가장 큰 값
        int rt = 0; // rt의 최댓값: data를 합한 값 (m = 1)

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
            rt += data[i];
            if (lt < data[i]) {
                lt = data[i];
            }
        }

        while (lt <= rt) {
            int mid = (lt + rt) / 2;
            
            int cnt = 1;
            int tmp = 0;
            for (int i = 0; i < n; i++) {
                if (tmp + data[i] <= mid) {
                    tmp += data[i];
                } else {
                    tmp = data[i];
                    cnt++;
                }
            }

            if (cnt <= m) {
                rt = mid - 1;
            } else {
                lt = mid + 1;
            }
        }

        bw.write(lt + "");

        br.close();
        bw.flush();
        bw.close();
    }
}