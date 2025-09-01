import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            nums[i] = Integer.parseInt(br.readLine());
            sum += nums[i];
        }

        Arrays.sort(nums);
        int surplus = sum - 100;

        int lt = 0;
        int rt = 8;
        while (nums[lt] + nums[rt] != surplus) {
            if (nums[lt] + nums[rt] > surplus) {
                rt--;
            } else if  (nums[lt] + nums[rt] < surplus) {
                lt++;
            } else {
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            if (i != lt && i != rt) {
                sb.append(nums[i]).append('\n');
            }
        }

        System.out.println(sb);
    }

}