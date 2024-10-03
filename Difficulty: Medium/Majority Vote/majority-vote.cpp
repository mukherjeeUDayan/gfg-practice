//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to find the majority elements in the array
    vector<int> findMajority(vector<int>& nums) {
        // Your code goes here.
        unordered_map<int, int>mp;
        vector<int>answ;
        int n= nums.size();
        for(auto it : nums){
            mp[it]++;
        }
        for(auto it : mp){
            if(it.second > (n/3)){
                answ.push_back(it.first);
            }
        }
        if(answ.empty()){
            return {-1};
        }
        sort(answ.begin(), answ.end());
        return answ;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        vector<int> ans = ob.findMajority(nums);
        for (auto &i : ans)
            cout << i << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends