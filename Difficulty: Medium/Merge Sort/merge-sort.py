#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
 
    def mergeSort(self,arr, l, r):
        #code here
        if (l==r):
            return 
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
        
    def merge(self,arr,l,mid,r):
        temp=[]
        left = l
        right = mid+1
        while left <= mid and right <= r:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left+=1
            else :
                temp.append(arr[right])
                right += 1
        while left <= mid :
            temp.append(arr[left])
            left+=1
        while right <= r :
            temp.append(arr[right])
            right += 1
        for i in range(l, r+1):
            arr[i] = temp[i-l]



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends