class Solution {
public:
    string minimizeError(vector<string>& a, int target) 
    {
        int n = a.size();
        int sum =0;
        vector<double> vec;
        //int count =0;
        for(int i=0;i<n;i++)
        {
            double f = stod(a[i]);
            int it = (int)f;
            if(it!=f)
            {
                if(it<0)
                    it--;
                vec.push_back(f-it);
                //count++;
            }
            sum+=it;
             
        }
        if(sum>target)
            return "-1";
        int rem = target - sum;
        if(vec.size()<rem)
            return "-1";
        
        nth_element(vec.begin(),vec.begin()+vec.size() -rem,vec.end());
        reverse(vec.begin(),vec.end());
        double ret =0.000;
        
        //cout<<count;
        for(int i=0;i<vec.size();i++)
        {
            if(i<rem)
            {
                ret += 1.000 - vec[i];   
            }
            else
            {
                ret+= vec[i]*1.000;
            }
            
            
        }
        string res_s = to_string(ret);
        return res_s.substr(0,res_s.length()-3);
    }
};