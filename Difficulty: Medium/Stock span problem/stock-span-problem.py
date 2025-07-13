class Solution:
    def calculateSpan(self, arr):
        #write code here       n = len(arr)
        n= len(arr)
        answ = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if not stack:
                answ[i] = i + 1
            else:
                answ[i] = i - stack[-1]
            stack.append(i)
        return answ