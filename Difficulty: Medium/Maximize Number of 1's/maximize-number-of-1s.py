class Solution:
    def maxOnes(self, arr, k):
        # code here
        mx=0
        left=0
        kk=k
        for right,ve in enumerate(arr):
            if ve==0:
                kk-=1
            if kk<0:
                if arr[left]==0:
                    kk+=1
                left+=1
            if kk>=0:
                mx=max(mx,right-left+1)
        return mx
        