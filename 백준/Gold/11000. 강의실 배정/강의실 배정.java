import java.util.*;
import java.io.*;

class Lecture {
    int start;
    int end;
    Lecture(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        Lecture[] lectures = new Lecture[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            lectures[i] = new Lecture(s, t);
        }

        // 시작 시간을 기준으로 오름차순 정렬
        Arrays.sort(lectures, Comparator.comparingInt(a -> a.start));

        // 끝나는 시간을 기준으로 오름차순으로 정렬되는 우선순위 큐
        PriorityQueue<Lecture> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a.end));

        // 첫 번째 강의를 넣음
        minHeap.offer(lectures[0]);

        for (int i = 1; i < lectures.length; i++) {
            Lecture earliestEndLecture = minHeap.peek();
            Lecture currentLecture = lectures[i];

            // 현재 강의의 시작 시간이 가장 일찍 끝나는 강의의 끝나는 시간보다 이른 경우
            // 새로운 강의실이 필요함
            if (currentLecture.start < earliestEndLecture.end) {
                minHeap.offer(currentLecture); // 새로운 강의실 할당
            } else {
                minHeap.poll(); // 이전 강의실 사용 가능
                minHeap.offer(currentLecture); // 기존 강의실 재사용
            }
        }

        bw.write(minHeap.size() + "\n"); // 필요한 최소 강의실의 수 반환
        bw.flush();
        bw.close();
        br.close();
    }
}