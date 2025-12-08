import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m = Integer.parseInt(br.readLine());

        int num = 0;

        StringBuilder sb = new StringBuilder();

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("all")) {
                num = (1 << 21) - 1;
                continue;
            } else if (command.equals("empty")) {
                num = 0;
                continue;
            }

            int val = Integer.parseInt(st.nextToken());

            switch (command) {
                case "add": {
                    num |= (1 << val);
                    break;
                }
                case "remove": {
                    num &= ~(1 << val);
                    break;
                }
                case "check": {
                    if ((num & (1 << val)) != 0) {
                        sb.append("1\n");
                    } else {
                        sb.append("0\n");
                    }
                    break;
                }
                case "toggle": {
                    num ^= (1 << val);
                    break;
                }
            }
        }

        System.out.println(sb);
    }
}