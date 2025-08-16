class Solution:

	def findLargest(self, arr):
	    # code here
	    st=list(map(str,arr))
        st.sort(key=lambda x : x*10 ,reverse=True)
        result="".join(st)
        if result[0]=="0":
            return 0
        else:
            return result
	    