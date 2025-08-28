import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        String[] line = br.readLine().split(" ");
        int a = Integer.parseInt(line[0]);
        int b = Integer.parseInt(line[1]);
        int c = Integer.parseInt(line[2]);

        int addMod = (a + b) % c;
        int mulMod = (a * b) % c;
        sb.append(addMod).append('\n');
        sb.append(addMod).append('\n');
        sb.append(mulMod).append('\n');
        sb.append(mulMod).append('\n');

        System.out.println(sb);
    }
}