import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String test = "";

        while ((test = br.readLine())!= null){
            int x = Integer.parseInt(test) * 10000000;
            int n = Integer.parseInt(br.readLine());
            int[] legos = new int[n];    

            for (int i = 0; i < n; i++) {
                legos[i] = Integer.parseInt(br.readLine());
            }

            Arrays.sort(legos);

            int lt = 0;
            int rt = n - 1;

            boolean blocked = false;
            while (lt < rt) {
                if (legos[lt]+ legos[rt] < x) {
                    lt++;
                } else if (legos[lt]+ legos[rt] > x) {
                    rt--;
                } else {
                    blocked = true;
                    bw.write("yes " + legos[lt] + " " + legos[rt]);
                    break;
                }
            }

            if (!blocked) {
                bw.write("danger");
            }

            test = null;
            bw.newLine();
            bw.flush();
        }
    }
}