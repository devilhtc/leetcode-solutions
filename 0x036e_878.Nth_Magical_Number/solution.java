class Solution {
    long MOD = 1000000007;
    
    public int nthMagicalNumber(int N, int A, int B) {
        // trivial case, A == B, so the N-th largest is N * A
        if (A == B) {
            return (int) ((((long) A) * ((long) N)) % MOD);
        }
        // switching A and B is just the same, we can enforce A < B
        if (A > B) {
            return nthMagicalNumber(N, B, A);
        }
        // now A < B
        
        // divide by gcd
        int c = gcd(A, B);
        long a = (long) (A / c);
        long b = (long) (B / c);
        
        // determine how many cycles are there
        long cycles = ((long) N) / (a + b - 1);
        long n = ((long) N) % (a + b - 1);
        
        // base case, solve it by binary search
        long result = nthMagicalNumberLong(n, a, b);
        
        // put the result together
        return (int) ((a * b * cycles * ((long) c) + result * ((long) c)) % MOD);
    }
    
    private long nthMagicalNumberLong(long n, long a, long b) {
        // trivial cases
        if (n == 0) return 0;
        if (a == 1) return n;
        
        // now n > 0, n < a + b - 1 and a < b and gcd(a, b) = 1
        // use binary search and some math to determine the result
        long lo = a - 1;
        long hi = a * b + 1;
        long result = 0;
        while (lo < hi) {
            long mi = (lo + hi) / 2;
            if (mi / a + mi / b > n) {
                hi = mi;
                continue;
            } else if (mi / a + mi / b < n) {
                lo = mi;
                continue;
            } else {
                // hooray, we've located the number range!
                // the number must satisfy the condition
                // num / a + num / b = n and (num % a == 0 or num % b == 0)
                // hence the maximum of (mi / a) * a and (mi / b) * b must be the num
                // since for num - 1, the condition will fail
                long x = mi / a;
                long y = mi / b;
                result = Math.max(x * a, y * b) % MOD;
                break;
            }
        }
        return result;
    }
    
    // greatest common divisor
    private int gcd(int a, int b) {
       if (b == 0) return a;
       return gcd(b, a % b);
    }
}