import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static long[] egcd(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] t = egcd(b, a % b);
        long g = t[0], x1 = t[1], y1 = t[2];
        return new long[]{g, y1, x1 - (a / b) * y1};
    }
    
    static long modInv(long a, long m) {
        long[] r = egcd(a, m);
        long x = r[1] % m;
        if (x < 0) x += m;
        return x;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long e = Long.parseLong(st.nextToken());
        long s = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());
        
        long[] mods = {15, 28, 19};
        long M = 1;
        for (long md : mods) M *= md;
        
        long r1 = e % 15;  // 0..14
        long r2 = s % 28;  // 0..27
        long r3 = m % 19;  // 0..18
        long[] residues = {r1, r2, r3};
        
        long[] Ms = { M / mods[0], M / mods[1], M / mods[2] };
        
        long[] invs = new long[3];
        for (int i = 0; i < 3; i++) {
            long a_i = Ms[i] % mods[i];
            invs[i] = modInv(a_i, mods[i]);
        }
        
        long k = 0;
        for (int i = 0; i < 3; i++) {
            long term = (residues[i] * (Ms[i] % M)) % M;
            term = (term * (invs[i] % M)) % M;
            k = (k + term) % M;
        }
        
        if (k == 0) k = M;

        System.out.println(k);
    }
}