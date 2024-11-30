//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function is to check whether two strings are anagram of each other or not.
    bool areAnagrams(string& s1, string& s2) {
        // Your code here
        int n1= s1.length();
        if(n1 != s2.length()){
            return false;
        }
        int chs[26]={0};
        for(int i=0; i<n1; i++){
            chs[s1[i]-'a']++;
        }
        for(int i=0; i<n1; i++){
            int idx= s2[i]-'a';
            if(chs[idx]==0){
                return false;
            }
            chs[idx]--;
        }
        return true;
        
    }
};

//{ Driver Code Starts.

int main() {

    int t;

    cin >> t;

    while (t--) {
        string c, d;

        cin >> c >> d;
        Solution obj;
        if (obj.areAnagrams(c, d))
            cout << "true" << endl;
        else
            cout << "false" << endl;
        cout << "~" << endl;
    }
}

// } Driver Code Ends