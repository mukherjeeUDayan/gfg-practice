#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        
        pref={}
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==0:
                return True
            elif sum in pref:
                return True
            if sum not in pref:
                pref[sum]=True
                
        return False