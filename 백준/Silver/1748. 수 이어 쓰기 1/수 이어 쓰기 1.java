import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Integer.parseInt(br.readLine());

        long result = 0;

        long temp = n;
        long digit = 0;
        while (temp != 0 ) {
            temp = temp / 10;
            digit++;
        }


        for (int i = 0; i < digit - 1; i++) {
            result += (i + 1) * 9 * pow(10, i);
        }


        result += (n - pow(10, digit-1) + 1) * (digit);

        System.out.println(result);
    }

    static long pow(long a, long b) {
        long result = 1;
        for (int i = 0; i < b; i++) {
            result *= a;
        }

        return result;
    }
}