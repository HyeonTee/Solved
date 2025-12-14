import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<String> result = new ArrayList<>();

        HashSet<String> memo = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            memo.add(name);
        }

        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            if (memo.contains(name)) {
                result.add(name);
            }
        }

        Collections.sort(result);

        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (String name : result) {
            sb.append(name).append("\n");
            cnt++;
        }

        System.out.println(cnt);
        System.out.println(sb);
    }
}