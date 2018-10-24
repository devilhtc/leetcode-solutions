public class Solution {
    public int firstMissingPositive(int[] nums) {
        removeZeros(nums);
        int l=nums.length;
        for (int i=0;i<l;i++) {
            
            int c=nums[i];
            while (c!=0) {
                // get index?
                if (c>0 && c<l+1) {
                    // is a valid positive number
                    int d=nums[c-1];
                    nums[c-1]=0;
                    c=d;
                } else {
                    c=0;
                }
               
            }
        }
        
        return firstMissingHelper(nums);
    }
    
    
    private int firstMissingHelper(int[] nums) {
        for (int i=0;i<nums.length;i++) {
            if (nums[i]!=0) {
                return i+1;
            }
        }
        return nums.length+1;
        
        
    }
    private void removeZeros(int[] nums) {
        for (int i=0;i<nums.length;i++) {
            if (nums[i]==0) {
                nums[i]=-1;
            }
        }
    }
}