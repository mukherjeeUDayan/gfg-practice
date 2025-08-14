class Solution {
  public:
    vector<vector<int>> insertInterval(vector<vector<int>> &iv,
                                       vector<int> &ni) {
        // code here
        vector<vector<int>> ans;
        int i = 0, n = iv.size();

        // Step 1: add all intervals before ni
        while (i < n && iv[i][1] < ni[0]) {
            ans.push_back(iv[i]);
            i++;
        }

        // Step 2: merge overlaps
        while (i < n && iv[i][0] <= ni[1]) {
            ni[0] = min(ni[0], iv[i][0]);
            ni[1] = max(ni[1], iv[i][1]);
            i++;
        }
        ans.push_back(ni);

        // Step 3: add remaining
        while (i < n) {
            ans.push_back(iv[i]);
            i++;
        }

        return ans;
    }
};