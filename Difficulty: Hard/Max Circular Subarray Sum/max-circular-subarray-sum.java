//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Sorting {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            int arr[] = new int[str.length];
            for (int i = 0; i < str.length; i++) arr[i] = Integer.parseInt(str[i]);
            System.out.println(new Solution().circularSubarraySum(arr));
            // System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {

    // a: input array
    // n: size of array
    // Function to find maximum circular subarray sum.
    public int circularSubarraySum(int arr[]) {

        // Your code here
        int n  = arr.length;
        int mini = Integer.MAX_VALUE;
        int maxi = Integer.MIN_VALUE;
        int sum1 = 0, sum2 = 0, total = 0;
        for(int i = 0;i<n;i++){
            sum1+=arr[i];
            sum2+=arr[i];
            total +=arr[i];
            if(sum2>0) sum2 = 0;
            else mini = Math.min(mini,sum2);
            if(sum1<0) sum1 = 0;
            else maxi = Math.max(maxi,sum1);
        }
        return Math.max(maxi,total-mini);
        
    }
}
