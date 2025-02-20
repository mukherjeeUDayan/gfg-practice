//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        while (t-- > 0) {
            String s = sc.nextLine();
            String[] parts = s.split(" ");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) {
                nums[i] = Integer.parseInt(parts[i]);
            }
            Solution ob = new Solution();
            ArrayList<Double> ans = ob.getMedian(nums);
            for (double i : ans) {
                System.out.printf("%.1f ", i);
            }
            System.out.println();
            System.out.println("~");
        }
        sc.close();
    }
}

// } Driver Code Ends


class Solution {
    public ArrayList<Double> getMedian(int[] arr) {
        // code here

        int n = arr.length;
        // Max-heap (low) and Min-heap (high)
        PriorityQueue<Integer> low = new PriorityQueue<>(Collections.reverseOrder()); // max-heap
        PriorityQueue<Integer> high = new PriorityQueue<>(); // min-heap
        ArrayList<Double> res = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int num = arr[i];

            // Add number to the appropriate heap
            if (low.isEmpty() || num <= low.peek()) {
                low.offer(num); // Add to max-heap (low)
            } else {
                high.offer(num); // Add to min-heap (high)
            }

            // Balance the heaps
            if (low.size() > high.size() + 1) {
                high.offer(low.poll()); // Move the root from low to high
            } else if (high.size() > low.size()) {
                low.offer(high.poll()); // Move the root from high to low
            }

            // Find the median
            if (low.size() > high.size()) {
                // If low has more elements, the median is the root of low
                res.add((double) low.peek());
            } else {
                // If both heaps have the same size, the median is the average of both roots
                res.add((low.peek() + high.peek()) / 2.0);
            }
        }
        
        return res;
    }
}