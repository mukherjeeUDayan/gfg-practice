//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

//User function Template for C++

class Solution {
  public:
    int makeProductOne(int arr[], int N) {
        // code here
        int n=N;
        int ans=0;
        int cnt_negone=0;
        int comm=0;
        for(int i=0;i<n;i++){
            if(abs(-1-arr[i])<abs(1-arr[i]))cnt_negone++;
            else if(arr[i]==0)comm++;
            ans+=min(abs(-1-arr[i]),abs(1-arr[i]));
        }
        if(cnt_negone%2==0)return ans;
        else if(comm!=0){
            //negone is odd....
            return ans;
        }
        else return ans+2;
        return ans;
        
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        
        int arr[N];
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution ob;
        cout << ob.makeProductOne(arr,N) << endl;
    
cout << "~" << "\n";
}
    return 0;
}
// } Driver Code Ends