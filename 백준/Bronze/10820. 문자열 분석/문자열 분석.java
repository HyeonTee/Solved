import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int lowers = 0, uppers = 0, nums = 0, blanks = 0;
            try {
                char[] chars = br.readLine().toCharArray();
                for (char c : chars) {
                    if ('a' <= c && c <= 'z') {
                        lowers++;
                    } else if ('A' <= c && c <= 'Z') {
                        uppers++;
                    } else if (c == ' ') {
                        blanks++;
                    } else {
                        nums++;
                    }
                }
                sb.append(lowers).append(" ").append(uppers).append(" ").append(nums).append(" ").append(blanks).append("\n");
            } catch (NullPointerException e) {
                break;
            }
        }

        System.out.println(sb);
    }
}