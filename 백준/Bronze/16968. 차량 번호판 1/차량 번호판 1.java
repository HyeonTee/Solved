import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String board = br.readLine();
        int result;
        if (board.charAt(0) == 'c') {
            result = 26;
        } else {
            result = 10;
        }
        for (int i = 1; i < board.length(); i++) {
            char c = board.charAt(i);
            if (c == 'c') {
                if (board.charAt(i-1) == board.charAt(i)) {
                    result *= 25;
                } else {
                    result *= 26;
                }
            } else {
                if (board.charAt(i-1) == board.charAt(i)) {
                    result *= 9;
                } else {
                    result *= 10;
                }
            }
        }

        System.out.println(result);
    }
}