class Solution:
    def toSec(self,string):
        h,m,s=list(map(int,string.split(":")))
        return h*60*60+m*60+s

    def minDifference(self, arr):
        maxTime=60*60*24
        time=[False]*(maxTime+1)
        for item in arr:
            second=self.toSec(item)
            if time[second]:
                return 0
            time[second]=True
        first=None
        prev=None
        ans=float("inf")
        for i in range(maxTime):
            if time[i]:
                if prev is not None:
                    ans=min(ans,i-prev)
                prev=i
                if first is None:
                    first=i
        return min(ans,maxTime-prev+first)
            
