import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Stack {
    int[] data;
    int top = 0;

    Stack(int n) {
        data = new int[n+1];
    }

    void push(int x) {
        data[++top] = x;
    }

    int pop() {
        if (top == 0) {
            return -1;
        }
        return data[top--];
    }

    int peek() {
        return data[top];
    }

    boolean isEmpty() {
        return top == 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = new int[n];
        Arrays.fill(result, -1);

        Stack stack = new Stack(n);
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (stack.isEmpty() || num <= nums[stack.peek()]) {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && num > nums[stack.peek()]) {
                    result[stack.pop()] = num;
                }
                stack.push(i);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(" ");
        }

        System.out.println(sb);
    }
}