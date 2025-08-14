class Solution:
    def mergeSort(self,arr,l,h):
        ans=0
        if l<h:
            mid=(l+h)//2
            ans+=self.mergeSort(arr,l,mid)
            ans+=self.mergeSort(arr,mid+1,h)
            ans+=self.merge(arr,l,mid,h)
        return ans
        
    def merge(self,arr,l,mid,h):
        ans=0
        j=mid+1
        for i in range(l,mid+1):
            while j<=h and arr[i]>2*arr[j]:
                j+=1
            ans+=(j-(mid+1))
        left=arr[l:mid+1]
        right=arr[mid+1:h+1]
        i,j,k=0,0,l
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return ans
    
    def countRevPairs(self, arr):
        return self.mergeSort(arr,0,len(arr)-1)
            # Code here