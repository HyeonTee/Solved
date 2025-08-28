import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] cnt = new int[26];
        String s = br.readLine();

        for (int i = 0, n = s.length(); i < n; i++) {
            char c = s.charAt(i);
            cnt[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder(26 * 3);
        for (int i = 0; i < 26; i++) {
            sb.append(cnt[i]);
            if (i < 25) sb.append(' ');
        }
        System.out.println(sb);
    }
}

