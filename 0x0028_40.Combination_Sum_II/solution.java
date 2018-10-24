public class Solution {
    private int[] a;
    private List<List<Integer>> output;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        output=new ArrayList<List<Integer>>();
        a=candidates;
        Arrays.sort(a);
        build(target,new ArrayList<Integer>(),0);
        return output;
    }
    
    private void build( int target, List<Integer> listNow, int start) {
        for (int i=start;i<a.length;i++) {
            List<Integer> listNext= new ArrayList<Integer>(listNow);
            if (a[i]==target) {
                listNext.add(a[i]);
                if (!output.contains(listNext)) output.add(listNext);
                
            } else if (a[i]<target) {
                listNext.add(a[i]);
                build(target-a[i],listNext,i+1);
            }
            
        }
    }
}