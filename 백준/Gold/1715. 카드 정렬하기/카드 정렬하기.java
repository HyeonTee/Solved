import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> cards = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            cards.add(Integer.parseInt(br.readLine()));
        }

        int ans = 0;
        if (n != 1) {
            for (int i = 0; i < n-1; i++) {
                int prevDeck = cards.poll();
                int currDeck = cards.poll();

                int newDeck = prevDeck + currDeck;
                ans += newDeck;
                cards.add(newDeck);
            }
        }

        bw.write(ans + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
