public class Solution {
    public void nextPermutation(int[] nums) {
        int n=nums.length;
        if (n<2) return;
        int i = findLargestUnsorted(nums);
        if (i!=0) {
            int j=n-1;
            while (j>=i &&  nums[j]<=nums[i-1]) {
                j--;
            }
            swap(nums,i-1,j);
        }
        reverseSort(nums, i, n-1);
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }
    
    private int findLargestUnsorted(int[] nums) {
        int n=nums.length;
        int i=n-1;
        while (i>0 && nums[i-1]>=nums[i]) {
            i--;
        }
        return i;
        
    }
    
    private void reverseSort(int[] nums, int start, int end) {
        if(start>end)
            return;
        for (int i=start;i<=(end+start)/2;i++)
            swap(nums,i,start+end-i);
    }
 }                          