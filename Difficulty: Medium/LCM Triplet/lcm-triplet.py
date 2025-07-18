class Solution:
    def lcmTriplets(self, n):
        #code here
        if n<= 2:
            return n
        if n & 1:
            return n*(n-1)*(n-2)
        else:
            if n%3:
                return n*(n-1)*(n-3)
            else:
                return (n-1)*(n-2)*(n-3)