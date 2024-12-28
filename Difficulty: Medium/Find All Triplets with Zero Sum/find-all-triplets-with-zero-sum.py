#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        n=len(arr)
        d=dict()

        for i in range(n):
            for j in range(i+1,n):
                s=arr[i]+arr[j]
                if s in d:
                    d[s].append([i,j])
                else:
                    d[s]=[[i,j]]
    
        # print(d)
        answ=set()

        for i in range(n):
            rem=-arr[i]
            # print(rem)
            if rem in d:
                for j in d[rem]:
                    if i==j[0] or i==j[1]:
                        continue
                    else:
                        ele=[i,j[0],j[1]]
                        ele.sort()
                        answ.add(tuple(ele))
            
        answ=[list(i) for i in answ]
        return answ

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends