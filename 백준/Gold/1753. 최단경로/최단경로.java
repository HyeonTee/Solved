import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine()) - 1;

        Map<Integer, Map<Integer, Integer>> edges = new HashMap<>();
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int weight = Integer.parseInt(st.nextToken());

            edges.putIfAbsent(a, new HashMap<>());
            // 출발, 도착이 같은 간선이 있는 경우를 고려해야 함!!!!!!!!!!!!!
            if (edges.get(a).containsKey(b)) {
                if (edges.get(a).get(b) > weight) {
                    edges.get(a).put(b, weight);
                }
            } else {
                edges.get(a).put(b, weight);
            }
        }

        int[] dist = new int[v];
        boolean[] visited = new boolean[v];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        PriorityQueue<int[]> pQ = new PriorityQueue<>(Comparator.comparingInt(arr -> arr[1]));
        pQ.offer(new int[]{k, 0});

        while (!pQ.isEmpty()) {
            int[] current = pQ.poll();
            int vertex = current[0];
            int distance = current[1];

            if (visited[vertex]) continue;

            if (edges.containsKey(vertex)) {
                for (Map.Entry<Integer, Integer> entry : edges.get(vertex).entrySet()) {
                    int nextVertex = entry.getKey();
                    int weight = entry.getValue();

                    if (dist[nextVertex] > distance + weight) {
                        dist[nextVertex] = distance + weight;
                        pQ.offer(new int[]{nextVertex, dist[nextVertex]});
                    }
                }
            }

            visited[vertex] = true;
        }

        for (int i = 0; i < v; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                bw.write("INF\n");
            } else {
                bw.write(dist[i] + "\n");
            }
        }

        bw.flush();
        bw.close();
    }
}