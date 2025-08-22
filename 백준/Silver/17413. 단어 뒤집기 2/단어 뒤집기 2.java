import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder answer = new StringBuilder();
        StringBuilder word = new StringBuilder();
        boolean inTag = false;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == '<') {
                answer.append(word.reverse());
                word.setLength(0);

                inTag = true;
                answer.append(ch);
            } else if (ch == '>') {
                inTag = false;
                answer.append(ch);
            } else if (inTag) {
                answer.append(ch);
            } else {
                if (ch == ' ') {
                    answer.append(word.reverse()).append(' ');
                    word.setLength(0);
                } else {
                    word.append(ch);
                }
            }
        }

        answer.append(word.reverse());

        System.out.print(answer);
    }
}