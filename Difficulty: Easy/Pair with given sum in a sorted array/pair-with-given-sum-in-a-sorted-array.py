#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        n=len(arr)
        start=0
        end=n-1
        count=0
        while(start<end):
            sums=arr[start]+arr[end];
            if(sums>target):
                end-=1
            elif(sums<target):
                start+=1
            else:
                ele1=arr[start]
                ele2=arr[end]
                count1=0
                count2=0
                while(start<=end and arr[start]==ele1):
                    count1+=1
                    start+=1
                while(start<=end and arr[end]==ele2):
                    count2+=1
                    end-=1
                if(ele1==ele2):
                    count+=count1*(count1-1)/2
                else:
                    count+=count1*count2
        return int(count)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends