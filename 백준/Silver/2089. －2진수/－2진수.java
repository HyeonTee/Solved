import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        if (n == 0) {
            System.out.println(0);
        } else {
            while (n != 1) {
                int quotient = n / -2;
                int remainder = n % -2;
                if (remainder == -1) {
                    quotient++;
                    remainder = 1;
                }
                n = quotient;
                sb.append(remainder);
            }
            sb.append(n);
            System.out.println(sb.reverse());
        }

    }
}