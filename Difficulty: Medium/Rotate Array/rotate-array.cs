//{ Driver Code Starts
using System;
using System.Collections.Generic;

// Position this line where user code will be pasted.

class Program {
    static void Main() {
        int t = int.Parse(Console.ReadLine()); // Number of test cases
        for (int i = 0; i < t; i++) {
            // Reading input array
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int d = int.Parse(Console.ReadLine());

            Solution solution = new Solution();
            solution.RotateArr(arr, d); // Reverse the array in place

            // Output formatting
            int n = arr.Length;
            for (int j = 0; j < n; j++) {
                if (j == n - 1) {
                    // Print last element with a newline
                    Console.WriteLine(arr[j]);
                } else {
                    // Print element followed by a space
                    Console.Write(arr[j] + " ");
                }
            }
            Console.WriteLine("~");
        }
    }
}

// } Driver Code Ends


// User function Template for C#

class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    public void RotateArr(int[] arr, int d) {
        // Code Here
        int n = arr.Length;

        // Handle the case where d > size of array
        d %= n;

        // Reverse the first d elements
        reverse(arr, 0, d - 1);

        // Reverse the remaining n-d elements
        reverse(arr, d, n - 1);

        // Reverse the entire array
        reverse(arr, 0, n - 1);
    }

    // Function to reverse a portion of the array
    static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
    }
    }
    
}