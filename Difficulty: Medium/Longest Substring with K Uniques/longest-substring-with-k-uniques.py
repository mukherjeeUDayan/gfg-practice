class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l=len(s)
        d={}
        curr_start=0
        max_len=-1
        curr_len=0
        i=0
        for i in range(l):
            d[s[i]]=d.get(s[i],0)+1
            
            # Shrink window if distinct chars > k
            while len(d)>k:
                d[s[curr_start]]-=1
                if d[s[curr_start]]==0:
                    del d[s[curr_start]]
                curr_start+=1
            
            # If window has exactly k distinct chars, update max_len
            if len(d) == k:
                max_len = max(max_len, i - curr_start + 1)
            
        return max_len
        
        