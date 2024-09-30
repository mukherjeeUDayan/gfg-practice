//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];
            String[] inputLine = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            System.out.println(new Solution().maxProduct(arr));
        }
    }
}

// } Driver Code Ends


class Solution {
    // Function to find maximum product subarray
    long maxProduct(int[] arr) {
        // code here

        long maxi=arr[0];
        long currMax= arr[0];
        long currMin= arr[0];
        for(int i=1; i<arr.length; i++){
            if(arr[i]<0){
                long temp= currMax;
                currMax= currMin;
                currMin= temp;
            }
            currMax= Math.max(arr[i], currMax*arr[i]);
            currMin= Math.min(arr[i], currMin*arr[i]);
            maxi=Math.max(maxi,currMax);
        }
        return maxi;
    }
}