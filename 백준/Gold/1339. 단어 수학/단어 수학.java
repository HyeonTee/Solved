import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Map<Character, Integer> dict = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String numStr = br.readLine();
            int len = numStr.length();
            for (int j = 0; j < len; j++) {
                char alphabet = numStr.charAt(j);
                if (dict.containsKey(alphabet)) {
                    dict.put(alphabet, dict.get(alphabet) + (int) Math.pow(10, len - j - 1));
                } else {
                    dict.put(alphabet, (int) Math.pow(10, len - j - 1));
                }
            }
        }

        int answer = 0;

        List<Integer> values = new ArrayList<>(dict.values());
        Collections.sort(values, Collections.reverseOrder());
        int x = 9;
        for (int value : values) {
            answer += value * x;
            x--;
        }
        
        bw.write(answer + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}