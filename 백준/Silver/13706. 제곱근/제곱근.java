import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        BigInteger num = new BigInteger(br.readLine());

        BigInteger lt = new BigInteger("1");
        BigInteger rt = num;
        BigInteger mid = null;

        while (true) {
            mid = lt.add(rt).divide(BigInteger.TWO);
            int result = mid.multiply(mid).compareTo(num);
            if (result == 1) {
                rt = mid.subtract(BigInteger.ONE);
            } else if (result == -1) {
                lt = mid.add(BigInteger.ONE);
            } else {
                break;
            }
        }

        bw.write(mid.toString());

        br.close();
        bw.flush();
        bw.close();
    }
}