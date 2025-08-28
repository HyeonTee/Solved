import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] count = new int[26];
        Arrays.fill(count, -1);
        char[] charArr = br.readLine().toCharArray();
        for (int i = 0; i < charArr.length; i++) {
            if (count[charArr[i] - 'a'] == -1) {
                count[charArr[i] - 'a'] = i;
            }
        }

        for (int i = 0; i < 26; i++) {
            sb.append(count[i]).append(" ");
        }

        System.out.println(sb);
    }
}