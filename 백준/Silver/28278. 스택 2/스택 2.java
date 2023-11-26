import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<Integer>();
        StringBuilder ans = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("1")) {
                stack.push(Integer.parseInt(st.nextToken()));
            } else if (command.equals("2")) {
                if (stack.isEmpty()) {
                    ans.append("-1\n");
                } else {
                    ans.append(stack.pop()).append("\n");
                }
            } else if (command.equals("3")) {
                ans.append(stack.size()).append("\n");
            } else if (command.equals("4")) {
                if (stack.isEmpty()) {
                    ans.append("1\n");
                } else {
                    ans.append("0\n");
                }
            } else if (command.equals("5")) {
                if (stack.isEmpty()) {
                    ans.append("-1\n");
                } else {
                    ans.append(stack.lastElement()).append("\n");
                }
            }
        }
        System.out.println(ans);
    }
}
