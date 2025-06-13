#User function Template for python3

class Solution:
    def kokoEat(self,arr,k):
        # Code here
        l , r = 1 , max(arr)
        res = 0
        def canEatBanana(h):
            count = 0
            for n in arr:
                count+=math.ceil(n/h)
            return count<=k
        while l <= r:
            mid = (l+r)//2
            if canEatBanana(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res