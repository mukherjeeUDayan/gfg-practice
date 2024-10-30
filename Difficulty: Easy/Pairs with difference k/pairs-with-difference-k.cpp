//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:
    /* Returns count of pairs with difference k  */
    int countPairsWithDiffK(vector<int>& arr, int k) {
        // code here
        sort(arr.begin(),arr.end());
        int low=0;
        int high=1;
        int ans=0;
        while(high<arr.size())
        {
            if (arr[high]-arr[low]==k)
            {
                low++;
                high++;
                int cnt1=1;
                int cnt2=1;
                while(high<arr.size() && arr[high]==arr[high-1])
                {
                    cnt2++;
                    high++;
                }
                while(low<high && arr[low-1]==arr[low])
                {
                    cnt1++;
                    low++;
                }
                
                ans+=cnt1*cnt2;
            }
            else if (arr[high]-arr[low]<k) high++;
            else low++;
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string ks;
        getline(cin, ks);
        int k = stoi(ks);
        Solution ob;
        auto ans = ob.countPairsWithDiffK(arr, k);
        cout << ans << "\n";
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends