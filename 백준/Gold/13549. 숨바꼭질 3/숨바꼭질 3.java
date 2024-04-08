import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] time = new int[100001];
        Arrays.fill(time, 9999999);
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(n);
        time[n] = 1;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            int[] move = {curr + 1, curr - 1, curr * 2};
            for (int i=0; i<3; i++) {
                int next = move[i];
                if (inRange(next)) {
                    if (i == 2 && time[next] > time[curr]) {
                        time[next] = time[curr];
                        queue.add(next);
                    } else {
                        if (time[next] > time[curr] + 1) {
                            time[next] = time[curr] + 1;
                            queue.add(next);
                        }
                    }
                }
            }
        }
        System.out.println(time[k] - 1);
    }

    static boolean inRange(int x) {
        return x >= 0 && x <= 100000;
    }
}