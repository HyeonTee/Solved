import java.util.*;

public class Main {
    static int n;
    static int k;
    static int[] graph = new int[100001];
    static int[] time = new int[100001];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();

        bfs();

        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        stack.push(k);
        int index = k;

        while (index != n) {
            stack.push(graph[index]);
            index = graph[index];
        }

        // 최종 출력
        sb.append(time[k] - 1 + "\n");
        while (!stack.isEmpty()) {
            sb.append(stack.pop() + " ");
        }

        System.out.println(sb);

    }

    static void bfs() {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(n);
        time[n] = 1;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            if (curr == k) return;

            int[] move = {curr + 1, curr - 1, curr * 2};

            for (int i=0; i<3; i++) {
                int next = move[i];

                if (inRange(next) && time[next] == 0) {
                    queue.add(next);
                    time[next] = time[curr] + 1;
                    graph[next] = curr;
                }
            }
        }
    }
    static boolean inRange(int x) {
        return x >= 0 && x <= 100000;
    }
}