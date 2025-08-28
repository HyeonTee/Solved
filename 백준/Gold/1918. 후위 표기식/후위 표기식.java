import java.io.*;

public class Main {
    static int prec(char op) {
        if (op == '+' || op == '-') return 1;
        if (op == '*' || op == '/') return 2;
        return 0; // '(' 등
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] expr = br.readLine().toCharArray();
        char[] stack = new char[expr.length];
        int top = -1;

        StringBuilder sb = new StringBuilder(expr.length);

        for (char c : expr) {
            if ('A' <= c  && c <= 'Z') {
                sb.append(c);
            } else if (c == '(') {
                stack[++top] = c;
            } else if (c == ')') {
                while (top >= 0 && stack[top] != '(') {
                    sb.append(stack[top--]);
                }
                top--;
            } else {
                while (top >= 0 && prec(stack[top]) >= prec(c)) {
                    if (stack[top] == '(') break;
                    sb.append(stack[top--]);
                }
                stack[++top] = c;
            }
        }

        while (top >= 0) {
            sb.append(stack[top--]);
        }

        System.out.println(sb);
    }
}