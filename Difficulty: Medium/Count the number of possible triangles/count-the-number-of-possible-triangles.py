#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n,ans=len(arr),0
        for i in range(n-1,1,-1):
            l,h=0,i-1
            while l<h:
                if arr[l]+arr[h]>arr[i]:
                    ans+=(h-l)
                    h-=1
                else:
                    l+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends