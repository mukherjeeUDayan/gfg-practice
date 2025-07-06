class Solution {
  public:
    vector<int> nextLargerElement(vector<int> &arr) {
        // code here
        stack<int> s;
        vector<int> out(arr.size(), -1);
        for(int i=0; i < (arr.size() << 1); i++)
        {
            while(s.size() && (arr[s.top()] < arr[i % arr.size()]))
            {
                out[s.top()] = arr[i % arr.size()];
                s.pop();
            }
            s.push(i % arr.size());
        }
        return out;
    }
};