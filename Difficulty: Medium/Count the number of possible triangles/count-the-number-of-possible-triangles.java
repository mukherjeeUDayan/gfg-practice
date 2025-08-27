class Solution {
    public int countTriangles(int arr[]) {
        // code here
        int n=arr.length;
        if(n<3) return 0;
        int c=0;
        Arrays.sort(arr);
        for(int i=0;i<n-2;i++){
            int sideA=arr[i];
            for(int j=i+1;j<n-1;j++){
                int sideB=arr[j];
                int sum=sideA+sideB;
                int l=j+1,h=n-1,idx=-1;
                while(l<=h){
                    int mid=(l+h)>>1;
                    
                    if(arr[mid]<sum) {
                        l=mid+1;
                        idx=mid;
                    }
                    else h=mid-1;
                }
               if(idx!=-1) c+=idx-j;
                
            }
        }
        
        return c;
    }
}