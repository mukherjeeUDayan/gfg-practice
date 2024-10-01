#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        if not A and not B:
            return -1
        min_len=(len(B)//len(A))+(1 if len(B)% len(A)!=0 else 0)
        rep_A=A*min_len
        
        if B in rep_A:
            return min_len
            
        rep_A= A*(min_len + 1)
        if B in rep_A:
            return min_len +1;
        return -1;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends