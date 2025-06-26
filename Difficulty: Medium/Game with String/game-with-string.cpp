class Solution {
  public:
    int minValue(string &s, int k) {
        // code here
        unordered_map<char,int>mp;
        priority_queue<int>q;
        for(auto x:s)
        mp[x]++;
        for(auto x:mp)
        q.push(x.second);
        while(q.empty()==false && k>0){
            int ele=q.top();
            q.pop();
            k--;
            ele--;
            q.push(ele);
        }
        int sum=0;
        while(!q.empty()){
            sum+=q.top()*q.top();
            q.pop();
        }
        return sum;
    }
};