class Solution {
  public:
    bool isPossible(vector<int>& arr, int k) {
        // code here
        map<int, int>mp;
        priority_queue<int, vector<int>, greater<int>>pq;
        for(auto &a : arr)
        {
            mp[a]++;
            pq.push(a);
        }
        while(pq.size())
        {
            int tp = pq.top();
            int prev = mp[tp];
            while(mp[tp] >= prev)
            {
                prev = mp[tp];
                mp[tp]--;
                // prev = tp;
                tp++;
            }
            
            int diff = tp - pq.top();
            // cout<<"tp "<<tp<<" prev "<<pq.top()<<endl;
            if(diff < k)return false;
            while(pq.size() && mp[pq.top()] == 0)
            {
                pq.pop();
            }
        }
        return true;    
    }
};
