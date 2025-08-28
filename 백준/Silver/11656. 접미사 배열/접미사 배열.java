import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        String[] strs = new String[str.length()];
        for (int i = 0; i < str.length(); i++) {
            strs[i] = str.substring(i, str.length());
        }

        Arrays.sort(strs);
        for (String s : strs) {
            sb.append(s).append("\n");
        }

        System.out.println(sb);
    }
}