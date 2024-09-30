//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    int lengthOfLongestAP(vector<int>& arr) {
        // code here
        int n=arr.size(),maxi=1;
        vector<vector<int>> v(n,vector<int> (arr[n-1]-arr[0]+1,0));
        for(int i=0;i<n;i++){
            for(int j=i-1;j>=0;j--){
             int d=arr[i]-arr[j];
             if(v[j][d]==0)v[i][d]=2;
             else v[i][d]=v[j][d]+1;
             maxi=max(maxi,v[i][d]);
            }
        }
        return maxi;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        auto ans = ob.lengthOfLongestAP(arr);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends