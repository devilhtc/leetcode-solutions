public class Solution {
    public int jump(int[] nums) {
    	int l=nums.length;
    	if (l<2) {
    		return 0;
    	}
    	
    	int jumps=1;
    	int reach=nums[0];
    	int left=0;
    	int reach2=0;
    	while (reach<l-1) {
    		for (int i=left;i<reach+1;i++) {
    			reach2=Math.max(reach2, i+nums[i]);
    		}
    		jumps=jumps+1;
    		left=reach+1;
    		reach=reach2;
    	}
    	return jumps;
    }
	
}