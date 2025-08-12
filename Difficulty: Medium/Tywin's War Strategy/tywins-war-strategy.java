class Solution {
    public int minSoldiers(int[] arr, int k) {
        // code here
        int n = arr.length ;
        
        for(int i = 0 ; i < n ; i++)
        {
            arr[i] = (k - arr[i] % k) % k ;
        }
        Arrays.sort(arr);
        int sumi = 0 ;
        for(int i = 0 ; i < (n + 1) / 2 ; i++)
        {
            sumi += arr[i];
        }
        return sumi;
    }
}