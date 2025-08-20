import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        int idx = 1;
        boolean ok = true;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            while (idx <= num) {
                stack.push(idx++);
                sb.append("+\n");
            }

            if (stack.peek() == num) {
                stack.pop();
                sb.append("-\n");
            } else {
                ok = false;
            }
        }

        if (ok) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '\n') {
                sb.deleteCharAt(sb.length() - 1);
            }
            System.out.print(sb.toString());
        } else {
            System.out.println("NO");
        }
    }
}
