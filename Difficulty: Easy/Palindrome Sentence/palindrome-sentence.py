class Solution:
	def isPalinSent(self, s):
		# code here
		def pelcheck(st):
    	    l = 0
    	    r = len(st)-1
    	    while l<r:
    	        if st[l]!=st[r]:
    	            return False
    	        l+=1
    	        r-=1
    	    return True
		s = s.lower()
		s = "".join(s.split())
		s1 = ""
		for c in s:
		    if c.isalnum():
		        s1 += c
# 		print(s)
		q = pelcheck(s1)
		return q