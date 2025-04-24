#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 

        ones, twos = 0, 0
        for number in arr:
            twos |= ones & number
            ones ^= number
            common_bits = ones & twos
            ones &= ~common_bits
            twos &= ~common_bits
        return ones
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends