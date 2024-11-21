//{ Driver Code Starts
// Initial template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        // code here
        int i = 0;
        int j = i+1;
        int maxi = 0;
        int profit = 0;
        
        while(i < prices.size() && j < prices.size())
        {
            int buy = prices[i];
            int sell = prices[j];
             
            int diff = (sell - buy);
            if(diff >= maxi)
            {
                maxi = diff;
                j++;
            }
            else
            {
                i = j;
                j++;
                profit += maxi;
                maxi = 0;
            }
        }
        
        if(maxi > 0)
        {
            profit += maxi;
        }
        
        return profit;
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
        int n = arr.size();
        Solution ob;
        int res = ob.maximumProfit(arr);
        cout << res;

        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends