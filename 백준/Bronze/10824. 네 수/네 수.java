import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str);
		
		String a = st.nextToken();
		String b = st.nextToken();
		String c = st.nextToken();
		String d = st.nextToken();

		System.out.println(Long.parseLong(a+b) + Long.parseLong(c+d));
    }
}