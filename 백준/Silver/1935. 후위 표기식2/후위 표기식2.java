import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[] expr = br.readLine().toCharArray();
        
        double[] val = new double[26];
        for (int i = 0; i < n; i++) {
            val[i] = Double.parseDouble(br.readLine());
        }

        double[] stack = new double[expr.length];
        int top = -1;

        for (char c : expr) {
            if ('A' <= c && c <= 'Z') {
                stack[++top] = val[c - 'A'];
            } else {
                double a = stack[top--];
                double b = stack[top--];
                switch (c) {
                    case '+': stack[++top] = b + a; break;
                    case '-': stack[++top] = b - a; break;
                    case '*': stack[++top] = b * a; break;
                    case '/': stack[++top] = b / a; break;
                }
            }
        }

        System.out.printf("%.2f%n", stack[top]);
    }
}