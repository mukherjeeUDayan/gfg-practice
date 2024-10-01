//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for Java

class Solution {
  public:

    long findIndex(string& str) {
        // Your code goes here
        long count=0;
        for(int i=0; i<str.size(); i++){
            if(str[i] == ')'){
                count++;
            }
        }
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        string str;
        cin >> str;
        Solution ob;
        cout << ob.findIndex(str) << endl;
    }
}
// } Driver Code Ends