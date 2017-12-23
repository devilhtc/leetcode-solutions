class Solution {
    public int myAtoi(String str) {
        str = strip(str);
        if (str.length() == 0) return 0;
        long res = 0;
        long sign = 1;
        int start = 0;
        if (str.charAt(0) == '-') {
            sign = -1;
            start = 1;
        } else if (str.charAt(0) == '+') {
            start = 1;
        }
        for (int i = start; i < str.length(); i++) {
            int nextDigit = (int) (str.charAt(i) - '0');
            if (nextDigit < 0 || nextDigit > 9) break;
            res = res * 10 + (long)nextDigit;
            if (sign * res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (sign * res < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        }
        return (int) (sign*res);
    }
    
    private String strip(String str) {
        int start = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ' ') {
                start = i;
                break;
            }
        }
        return str.substring(start);
    } 
}