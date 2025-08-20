import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String init = br.readLine();
        int m = Integer.parseInt(br.readLine());

        // 최대 길이 = 초기 길이 + 최대 삽입 횟수 + 여유
        int cap = init.length() + m + 8;
        char[] left = new char[cap];
        char[] right = new char[cap];
        int lsz = init.length(); // left stack size (cursor is at lsz)
        int rsz = 0;             // right stack size

        // 초기 문자열을 왼쪽 스택에 채워두기
        init.getChars(0, init.length(), left, 0);

        String line;
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            char cmd = line.charAt(0);

            switch (cmd) {
                case 'L':
                    if (lsz > 0) {
                        right[rsz++] = left[--lsz];
                    }
                    break;
                case 'D':
                    if (rsz > 0) {
                        left[lsz++] = right[--rsz];
                    }
                    break;
                case 'B':
                    if (lsz > 0) {
                        lsz--;
                    }
                    break;
                case 'P':
                    // line 형식: "P x"
                    char ch = line.charAt(2);
                    left[lsz++] = ch;
                    break;
            }
        }

        // 결과 빌드: left 그대로 + right 역순
        StringBuilder sb = new StringBuilder(lsz + rsz);
        sb.append(left, 0, lsz);
        for (int i = rsz - 1; i >= 0; i--) sb.append(right[i]);

        System.out.print(sb);
    }
}