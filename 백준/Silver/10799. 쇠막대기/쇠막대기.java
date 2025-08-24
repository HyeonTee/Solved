import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int stack = 0;
        int answer = 0;

        for (int i = 0; i < str.length(); i++){
            if (str.charAt(i) == '(') {
                if (str.charAt(i + 1) == ')') {
                    answer += stack;
                } else {
                    stack++;
                }
            } else {
                if (str.charAt(i - 1) != '(') {
                    answer++;
                    stack--;
                }
            }
        }

        System.out.println(answer);
    }
}