class Solution:
    def numberOfPath(self, mat, k):
        # code here
        n, m = len(mat), len(mat[0])
        
        # Initialize 3D DP array with zeros
        dp = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
        
        # Base case: starting point
        if mat[0][0] <= k:
            dp[0][0][mat[0][0]] = 1
        
        # Fill DP table
        for i in range(n):
            for j in range(m):
                for coins in range(k+1):
                    if coins < mat[i][j]:
                        continue
                    val = coins - mat[i][j]
                    
                    # From top
                    if i > 0:
                        dp[i][j][coins] += dp[i-1][j][val]
                    
                    # From left
                    if j > 0:
                        dp[i][j][coins] += dp[i][j-1][val]
        
        # Result: number of paths reaching bottom-right with exactly k coins
        return dp[n-1][m-1][k]
        

