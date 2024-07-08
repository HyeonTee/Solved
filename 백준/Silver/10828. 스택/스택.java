import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Deque<Integer> stack = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("push")) {
                int num = Integer.parseInt(st.nextToken());
                stack.push(num);
            } else if (command.equals("pop")) {
                if (stack.size() == 0) {
                    bw.write(-1 + "\n");
                    bw.flush();
                } else {
                    bw.write(stack.pop() + "\n");
                    bw.flush();
                }
            } else if (command.equals("top")) {
                if (stack.size() == 0) {
                    bw.write(-1 + "\n");
                } else {
                    bw.write(stack.peek() + "\n");
                }
                bw.flush();
            } else if (command.equals("size")) {
                bw.write(stack.size() + "\n");
                bw.flush();
            } else if (command.equals("empty")) {
                if (stack.isEmpty()) {
                    bw.write(1 + "\n");
                } else {
                    bw.write(0 + "\n");
                }
                bw.flush();
            }
        }
        bw.close();
        br.close();
    }
}