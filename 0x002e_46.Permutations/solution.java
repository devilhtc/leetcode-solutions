public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> output=new ArrayList<List<Integer>>();
        if (nums.length==0) {
        	return output;
        } else {
        	List<Integer> arrayNow=new ArrayList<Integer>();
        	arrayNow.add(nums[0]);
        	output.add(arrayNow);
        }
        for (int i=1;i<nums.length;i++) {
            List<List<Integer>> next=new ArrayList<List<Integer>>();
            for (int j=0;j<output.size();j++) {
                
                for (int k=0;k<output.get(j).size()+1;k++) {
                	List<Integer> arrayNow=new ArrayList<Integer>(output.get(j));
                    arrayNow.add(k,nums[i]);
                    next.add(arrayNow);
                }
               
            }
            output=next;  
        }
        return output;
    }
}