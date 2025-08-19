import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            StringBuilder builder = new StringBuilder();

            while (st.hasMoreTokens()) {
                StringBuffer buffer = new StringBuffer(st.nextToken());
                builder.append(buffer.reverse()).append(" ");
            }

            bw.write(builder.toString().trim());
            bw.newLine();
        }

        bw.flush();
    }
}