import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] cities = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int budget = Integer.parseInt(br.readLine());

        int lt = budget / n;
        int rt = 0;
        for (int i = 0; i < n; i++) {
            int city = Integer.parseInt(st.nextToken());
            cities[i] = city;
            if (city > rt) {
                rt = city;
            }
        }

        while (lt <= rt) {
            int mid = (lt + rt) / 2;
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if (mid >= cities[i]) {
                    sum += cities[i];
                } else {
                    sum += mid;
                }
            }

            if (sum < budget) {
                lt = mid + 1;
            } else if (sum > budget) {
                rt = mid - 1;
            } else {
                rt = mid;
                break;
            }
        }

        bw.write(rt + "\n");

        br.close();
        bw.flush();
        bw.close();
    }
}