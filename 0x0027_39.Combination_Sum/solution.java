class Solution {
    List<List<Integer>> out;
    int t;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        out=new ArrayList();
        t=target;
        helper(new ArrayList<Integer>(), candidates, 0, 0);
        return out;
    }
    
    private void helper(List<Integer> list, int[] cand, int cur, int preSum) {
        if (preSum>t)   return;
        if (preSum==t) {
            out.add(new ArrayList(list));
            return;
        }
        if (cur>=cand.length) return;
        
        int num=cand[cur];
        
        for (int i=0; i*num+preSum<=t;i++) {
            if (i!=0) list.add(num);
            helper(list, cand, cur+1, preSum+num*i);
        }
        
        for (int i=0; i*num+preSum<=t;i++) {
            if (i!=0) list.remove(list.size()-1);
        }
        
    }
}