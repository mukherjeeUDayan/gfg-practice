//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int arr[][] = new int[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            new Solution().setMatrixZeroes(arr);
            for (int[] row : arr) {
                for (int val : row) {
                    System.out.print(val + " ");
                }
                System.out.println();
            }

            System.out.println("~");
        }
    }
}

// } Driver Code Ends


//Back-end complete function Template for Java
class Solution {
    private static class Info{
        int row;
        int col;
        public Info(int row,int col){
            this.row=row;
            this.col=col;
        }
    }
    public void setMatrixZeroes(int[][] mat) {
        List<Info> list=new ArrayList<>();
        for(int i=0;i<mat.length;i++){
            for(int j=0;j<mat[0].length;j++){
                if(mat[i][j]==0) list.add(new Info(i,j));
            }
        }
        
        for(int i=0;i<list.size();i++){
            Info info=list.get(i);
            int newRow=info.row;
            int newCol=info.col;
            for(int j=0;j<mat[0].length;j++){
                mat[newRow][j]=0;
            }
            for(int j=0;j<mat.length;j++){
                mat[j][newCol]=0;
            }
        }
    }
}