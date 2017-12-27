class Solution {
    public String minWindow(String S, String T) {
        int[][] dp = new int[S.length()][T.length()];
        int found = 0;
        for (int i =0;i<S.length();i++) {
            if (S.charAt(i) == T.charAt(0)) {
                found = i+1;
            }
            dp[i][0] = found;
        }
        
        for (int i = 1; i<S.length();i++) {
            for (int j = 1;j<T.length(); j++) {
                if (S.charAt(i) == T.charAt(j)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        
        int minlen = S.length() + 1;
        int minStart = 0;
        int minEnd = 0;
        for (int i =0;i<S.length();i++) {
            int cur = dp[i][T.length() - 1];
            if (cur != 0) {
                int curlen = i-cur + 1;
                if (curlen < minlen) {
                    minlen = curlen;
                    minStart = cur - 1;
                    minEnd = i + 1;
                }
            }
        }
            
        return S.substring(minStart, minEnd );
    }
}