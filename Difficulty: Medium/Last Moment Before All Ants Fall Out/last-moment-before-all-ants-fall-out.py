class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        ans = 0
        l, r = 0, n
        for i in left:
            ans = max(ans, i-l)
        for j in right:
            ans = max(ans, r-j)
        return ans