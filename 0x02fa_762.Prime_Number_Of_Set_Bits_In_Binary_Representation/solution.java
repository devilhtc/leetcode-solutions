class Solution {
    public int countPrimeSetBits(int L, int R) {
        int[] bits = new int[32];
        int count = 0;
        for (int i = 0; i < 32; i ++) {
            if ((L & (1 << i)) > 0) {
                bits[i] = 1;
                count += 1;
            } 
        }
        int out = isPrime(count) ? 1 : 0;
        for (int j = L + 1; j < R + 1; j++) {
            count += escalate(bits, 0);
            out += (isPrime(count) ? 1 : 0);
        }
        return out;
    }
    
    private int escalate(int[] bits, int cur) {
        if (bits[cur] == 0) {
            bits[cur] = 1;
            return 1;
        } else {
            bits[cur] = 0;
            return escalate(bits, cur + 1) - 1;
        }
    }
    
    private boolean isPrime(int n) {
        if (n == 0 || n == 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0) return false;
        return true;
    }
}