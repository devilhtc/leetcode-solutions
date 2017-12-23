class Solution {
    public int reverse(int x) {
        boolean isNegative = x<0;
        long xLong = (long) x;
        if (isNegative) xLong = -1*xLong;
        StringBuilder sb = new StringBuilder(Long.toString(xLong));
        sb.reverse();
        String reversed = (isNegative? "-":"") + sb.toString();
        long xLongReversed = Long.parseLong(reversed);
        if (xLongReversed > (long) Integer.MAX_VALUE || xLongReversed < (long) Integer.MIN_VALUE) return 0;
        return (int) xLongReversed;
    }
}