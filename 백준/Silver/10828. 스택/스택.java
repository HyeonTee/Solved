import java.io.*;
import java.util.*;

class Stack {
    int[] data = new int[10000];
    int size = 0;

    void push(int num) {
        data[size++] = num;
    }

    int pop() {
        if (size == 0) {
            return -1;
        }
        return data[--size];
    }

    int size() {
        return size;
    }

    int isEmpty() {
        return size == 0 ? 1 : 0;
    }

    int top() {
        if (size == 0) {
            return -1;
        }
        return data[size-1];
    }
}

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack stack = new Stack();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "push":
                    stack.push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    bw.write(String.valueOf(stack.pop()));
                    bw.newLine();
                    break;
                case "empty":
                    bw.write(String.valueOf(stack.isEmpty()));
                    bw.newLine();
                    break;
                case "size":
                    bw.write(String.valueOf(stack.size()));
                    bw.newLine();
                    break;
                case "top":
                    bw.write(String.valueOf(stack.top()));
                    bw.newLine();
                    break;
            }
        }

        bw.flush();
    }
}
