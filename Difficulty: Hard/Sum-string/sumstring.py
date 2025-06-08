class Solution:
    def isValid(self,a,b,remaining):
        if not remaining:
            return True
        sum_str=str(int(a)+int(b))
        if remaining.startswith(sum_str):
            return self.isValid(b,sum_str,remaining[len(sum_str):])
        return False
        
    def isSumString (self, s):
        n=len(s)
        for i in range(1,n):
            for j in range(i+1,n):
                a=s[:i]
                b=s[i:j]
                if (len(a)>1 and a[0]=="0") or (len(b)>1 and b[0]=="0"):
                    continue
                if self.isValid(a,b,s[j:]):
                    return True