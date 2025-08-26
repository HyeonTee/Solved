import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int[] result = new int[n];
        Arrays.fill(result, -1);

        int[] stack = new int[n];
        int top = -1;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            while (top >= 0 && map.get(num) > map.get(nums[stack[top]])) {
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