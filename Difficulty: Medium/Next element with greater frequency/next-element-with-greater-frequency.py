from collections import Counter
class Solution:
    def findGreater(self, arr):
        freq=Counter(arr)
        stack=[]
        n=len(arr)
        ans=[None]*n
        for i in range(n-1,-1,-1):
            while stack and freq[stack[-1]]<=freq[arr[i]]:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(arr[i])
        return ans