//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class Driver {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String arr1[] = br.readLine().split(" ");
            int[] a = new int[arr1.length];

            for (int i = 0; i < a.length; i++) a[i] = Integer.parseInt(arr1[i]);

            String arr2[] = br.readLine().split(" ");
            int[] b = new int[arr2.length];

            for (int i = 0; i < arr2.length; i++) b[i] = Integer.parseInt(arr2[i]);

            if (b.length == 1 && b[0] == 0) {
                b = new int[0];
            }
            double res = new Solution().medianOf2(a, b);

            if (res == (int)res)
                System.out.println((int)res);
            else
                System.out.println(res);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public double medianOf2(int a[], int b[]) {
        // Your Code Here
        int merged[] = new int[a.length+b.length];
        int i =0;
        int j = 0;
        int k = 0;//for merged array 
        while( i < a.length && j < b.length){
            if(a[i] < b[j]){
                merged[k++] = a[i++];
            }else{
                merged[k++] = b[j++];
            }
        }
        while( i < a.length){
            merged[k++] = a[i++];
        }
        while( j < b.length){
            merged[k++] = b[j++];
        }
        int n = merged.length;
        if(n % 2 == 0){
            return (merged[n/2 - 1] + merged[n/2])/2.0;
        }else{
            return merged[n/2];
        }
        
    }
}