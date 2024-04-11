import java.util.*;
import java.io.*;

public class Main {
    static int v, e, p;
    static Map<Integer, Map<Integer, Integer>> edges;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken()); // node 갯수
        e = Integer.parseInt(st.nextToken()); // edge 갯수
        p = Integer.parseInt(st.nextToken()) - 1; // target 위치

        edges = new HashMap<>();

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int distance = Integer.parseInt(st.nextToken());

            edges.putIfAbsent(a, new HashMap<>());
            edges.putIfAbsent(b, new HashMap<>());

            edges.get(a).put(b, distance);
            edges.get(b).put(a, distance);
        }

        if (dijkstra(0)[v-1] == dijkstra(0)[p] + dijkstra(p)[v-1]) {
            bw.write("SAVE HIM\n");
        } else {
            bw.write("GOOD BYE\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }

    static int[] dijkstra(int start) {
        int[] dist = new int[v];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<int[]> pQ = new PriorityQueue<>(Comparator.comparingInt(arr -> arr[1]));
        pQ.offer(new int[]{start, 0});
        while (!pQ.isEmpty()) {
            int[] curr = pQ.poll();
            int v = curr[0];
            int d = curr[1];
            if (edges.containsKey(v)) {
                for (Map.Entry<Integer, Integer> entry : edges.get(v).entrySet()) {
                    int nv = entry.getKey();
                    int nd = entry.getValue();

                    if (dist[nv] > d + nd) {
                        dist[nv] = d + nd;
                        pQ.offer(new int[]{nv, dist[nv]});
                    }
                }
            }
        }

        return dist;
    }
}