class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        for (int i = 0; i < p.length(); i++) {
            if (i >= 1 && p.charAt(i) == '*') dp[0][i+1] = dp[0][i-1];  
        }
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (j >= 1 && p.charAt(j) == '*') {
                    dp[i+1][j+1] = dp[i+1][j-1];
                    if (cmp(s.charAt(i), p.charAt(j-1))) dp[i+1][j+1] = dp[i][j-1] || dp[i][j+1] || dp[i+1][j+1];
                } else {
                    dp[i+1][j+1] = (cmp(s.charAt(i), p.charAt(j)) && dp[i][j]);
                }
            }
        }
        return dp[s.length()][p.length()];
    }

    private boolean cmp(char sc, char pc) {
        if (pc == '.') return true;
        return sc == pc;
    }
}