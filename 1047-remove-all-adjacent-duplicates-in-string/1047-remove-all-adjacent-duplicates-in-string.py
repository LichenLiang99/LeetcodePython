class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
                continue
            stack.append(c)
            
            
        
        return ''.join(stack)