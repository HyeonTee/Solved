import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder(br.readLine());
        int cursor = sb.length();

        int m = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "L":
                    if (cursor > 0) cursor--;
                    break;
                case "D":
                    if (cursor < sb.length()) cursor++;
                    break;
                case "B":
                    if (cursor > 0) {
                        sb.deleteCharAt(cursor - 1);
                        cursor--;
                    }
                    break;
                case "P":
                    String charToInsert = st.nextToken();
                    sb.insert(cursor, charToInsert);
                    cursor++;
                    break;
            }
        }

        System.out.println(sb);
    }
}
