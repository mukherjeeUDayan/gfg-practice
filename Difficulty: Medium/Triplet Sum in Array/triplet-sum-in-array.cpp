class Solution {
  public:
    bool hasTripletSum(vector<int> &arr, int target) {
        // Your Code Here
        sort(arr.begin(),arr.end());
        int n = arr.size();
        for(int i=0;i<n-2;i++)
        {
            int ans1 = arr[i];
            int j=i+1,k=n-1;
            while(j<k)
            {
                if(ans1+arr[j]+arr[k]==target)
                return true;
                else if(ans1+arr[j]+arr[k]<target)
                j++;
                else if(ans1+arr[j]+arr[k]>target) 
                k--;
            }
        }
        return false;
    }
};