import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] s = br.readLine().toCharArray();

        int stack = 0;
        int answer = 0;
        char prev = 0;

        for (char c : s) {
            if (c == '(') {
                stack++;
            } else {
                stack--;
                if (prev == '(') {
                    answer += stack;
                } else {
                    answer += 1;
                }
            }
            prev = c;
        }

        System.out.println(answer);
    }
}
