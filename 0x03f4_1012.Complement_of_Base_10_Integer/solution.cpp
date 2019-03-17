class Solution {
public:
    int bitwiseComplement(int N) {
        int hb = 0;
        for (int i = 0; i < 32; i++) {
            if ((N & (1 << i)) > 0) {
                hb = i;
            }
        }
        for (int i = 0; i < hb + 1; i++) {
            if ((N & (1 << i)) > 0) {
                N = N & ~(1 << i);
            } else {
                N = N | (1 << i);
            }
        }
        return N;
    }
};