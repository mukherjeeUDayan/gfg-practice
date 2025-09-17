class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        for i in s:
            if i == ']':
                expand = ''
                while stack[-1] != '[':
                    expand = stack.pop() + expand
                stack.pop()

                mul = ''
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
                
                stack.append(int(mul) * expand)
                continue
            
            stack.append(i)
            
        return ''.join(stack)