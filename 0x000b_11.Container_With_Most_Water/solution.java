class Solution {
    public int maxArea(int[] height) {
        int i=0, j=height.length-1;
        int curHeight=Math.min(height[i],height[j]);
        int curMaxArea=curHeight*(j-i);
        
        while (j>i) {
            while (j>i && height[i]<=curHeight) {
                i++;
            }
            while (j>i && height[j]<=curHeight) {
                j--;
            }
            curHeight=Math.min(height[i],height[j]);
            curMaxArea=Math.max(curMaxArea,curHeight*(j-i));
        }
        return curMaxArea;
    }
}