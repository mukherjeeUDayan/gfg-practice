#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        dp = [[0]*(r+1) for _ in range(n+1)]
  
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, r+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends