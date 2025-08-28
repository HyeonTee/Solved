import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] count = new int[26];
        char[] charArr = br.readLine().toCharArray();
        for (char c : charArr) {
            count[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            sb.append(count[i]).append(" ");
        }

        System.out.println(sb);
    }
}