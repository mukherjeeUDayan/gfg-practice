//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int minVal(int a, int b) {
        // code here
        int ans = 0, setB = __builtin_popcount(b);
        if(setB == 0)
            return 0;
        // first move from backside
        for(int i = 31;i >= 0 && setB > 0; i--) {
            if(1<<i & a) {
                ans += (1<<i);
                setB--;
            }
        }
        // then move from frontside
        for(int i = 0;i < 32 && setB > 0; i++) {
            if(!(1<<i & a)) {
                ans += (1<<i);
                setB--;
            }
        }
        
        return ans;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;

        Solution ob;
        cout << ob.minVal(a, b);

        cout << "\n";
    
cout << "~" << "\n";
}

    return 0;
}
// } Driver Code Ends