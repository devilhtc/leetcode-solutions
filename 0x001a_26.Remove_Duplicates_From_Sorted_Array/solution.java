public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length==0) return 0;
        int count=1;
        int numNow=nums[0];
        for (int i=1;i<nums.length;i++) {
            if (numNow!=nums[i]) {
                nums[count]=nums[i];
                numNow=nums[i];
                count++;
                
            } 
        }
        return count;
    }
}