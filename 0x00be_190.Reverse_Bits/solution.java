public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        long n2 = (long)n;
        for (int i = 0; i < 16; i++) {
            int a = get(n2, i);
            int b = get(n2, 31 - i);
            n2 = set(n2, i, b);
            n2 = set(n2, 31 - i, a);
        }
        return (int)n2;
    }
    
    private int get(long n, int k) {
        long mask = 1;
        mask = mask << k;
        return (n & mask) == 0 ? 0 : 1;
    }
    
    private long set(long n, int k, int v) {
        long mask = 1;
        mask = mask << k;
        if (v == 1) {
            n = n | mask;
        } else {
            n = n & (~mask);
        }
        return n;
    }
}