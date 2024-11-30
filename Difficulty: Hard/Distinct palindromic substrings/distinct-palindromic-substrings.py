#User function Template for python3

class Solution:
    def palindromeSubStrs(self, Str):
        # code here
        p = set()
        n = len(Str)
        s=Str
    
        def expand(i, j):
            while 0 <= i and j < n and s[i] == s[j]:
                p.add(s[i : j + 1])
                i, j = i - 1, j + 1
    
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return len(p)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.palindromeSubStrs(Str))
        print("~")
# } Driver Code Ends