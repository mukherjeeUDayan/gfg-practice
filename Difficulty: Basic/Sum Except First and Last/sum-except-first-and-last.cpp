class Solution {
  public:
    /*You are required to complete this method*/
    int sumExceptFirstLast(vector<int>& arr) {
        // Your code here
        long long int answ=0;
        int n= arr.size();
        for(int i=1; i<n-1; i++){
            answ+=arr[i];
        }
        return answ;
    }
};