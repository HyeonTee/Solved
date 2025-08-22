import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] list = new int[n + 8];
        int lt = 0, rt = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "push":
                    list[rt++] = Integer.parseInt(st.nextToken());
                    break;

                case "pop":
                    if (lt == rt) sb.append("-1\n");
                    else sb.append(list[lt++]).append('\n');
                    break;

                case "size":
                    sb.append(rt - lt).append('\n');
                    break;

                case "empty":
                    if (lt == rt) sb.append("1\n");
                    else sb.append("0\n");
                    break;

                case "front":
                    if (lt == rt) sb.append("-1\n");
                    else sb.append(list[lt]).append('\n');
                    break;

                case "back":
                    if (lt == rt) sb.append("-1\n");
                    else sb.append(list[rt - 1]).append('\n');
                    break;
            }
        }
        System.out.print(sb);
    }
}