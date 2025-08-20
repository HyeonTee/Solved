import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < t; i++) {
            Stack<Character> stack = new Stack<>();
            String result = "YES";
            for (char c : br.readLine().toCharArray()) {
                if (c == '(') {
                    stack.push('(');
                } else {
                    if (stack.isEmpty()) {
                        result = "NO";
                        break;
                    } else {
                        if (stack.peek() == '(') {
                            stack.pop();
                        }
                    }
                }
            }
            
            if (!stack.isEmpty()) {
                result = "NO";
            }

            bw.write(result);
            bw.newLine();
        }

        bw.flush();
    }
}
