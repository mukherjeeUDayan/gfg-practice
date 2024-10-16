class Solution:
    def checkSorted(self, arr):
        #code here
        i=s=0

        while(i<len(arr)):

            if arr[i]==i+1:

                i+=1

            else:

                arr[arr[i]-1], arr[i]=arr[i], arr[arr[i]-1]   

                s+=1

                if s==3:

                    return False

        if s==2 or s==0:

            return True

        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends