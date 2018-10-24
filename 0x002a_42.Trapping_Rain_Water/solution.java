public class Solution {
    public int trap(int[] height) {
    	int l=height.length;
        if (l==0) {
            return 0;
        }
    	int[] a1=new int[l];
    	int[] a2=new int[l];
    	int max1=0;
    	int max2=0;
    	int j;
    	for (int i=0;i<l;i++) {
    		j=l-1-i;
    		if (height[i]>max1) {
    			max1=height[i];
    		}
    		a1[i]=max1;
    		if (height[j]>max2) {
    			max2=height[j];
    		}
    		a2[j]=max2;
    	}
    	int rain=0;
    	for (int i=0;i<l;i++) {
    		rain=rain+Math.min(a1[i], a2[i])-height[i];
    	}
    	return rain;
    }
}