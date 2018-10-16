public class Solution {
	private List<String> output;
	private int m;
    public List<String> generateParenthesis(int n) {
    	output=new ArrayList<String>();
    	m=n;
    	this.build("",0,0);
    	return output;
    }
    
    private void build(String s,int left,int right) {
    	if (s.length()==2*m) {
    		output.add(s);
    	} else {
    		String sNext=s.substring(0);
    		if (left<m) {
    			build(s+"(",left+1,right);
    		}
    		if (left>right) {
    			build(s+")",left,right+1);
    		}
    		
    	}
    }
}