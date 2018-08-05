class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int l = A.length;
        int[][] dp = new int[l][l];
        int out = 0;
        Map<Integer, Integer> index = new HashMap();
        for (int i = 0; i < l; i++) {
            index.put(A[i], i);
            for (int j = i + 1; j < l; j++) {
                int prev = A[j] - A[i];
                if (prev < A[i] && index.containsKey(prev)) {
                    dp[i][j] = dp[index.get(prev)][i] + 1;
                } else {
                    dp[i][j] = 2;
                }
                out = Math.max(dp[i][j], out);
            }
        }
        return out < 3 ? 0 : out;
    }
}