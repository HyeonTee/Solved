import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = "";
        ArrayList<Integer> inputList = new ArrayList<>();
        while ((s = br.readLine()) != null) {
            inputList.add(Integer.parseInt(s));
        }

        ArrayList<Integer> postOrdered = preToPost(inputList);
        for (int val : postOrdered) {
            bw.write(val + "\n");
        }

        bw.flush();

        bw.close();
        br.close();
    }

    static ArrayList<Integer> preToPost(ArrayList<Integer> preordered) {
        if (preordered.isEmpty()) {
            return new ArrayList<>();
        }
        int root = preordered.get(0);

        ArrayList<Integer> ltSubtree = new ArrayList<>();
        ArrayList<Integer> rtSubtree = new ArrayList<>();

        for (int val : preordered) {
            if (val < root) {
                ltSubtree.add(val);
            } else if (val > root) {
                rtSubtree.add(val);
            }
        }
        ArrayList<Integer> result = new ArrayList<>();
        result.addAll(preToPost(ltSubtree));
        result.addAll(preToPost(rtSubtree));
        result.add(root);

        return result;
    }
}