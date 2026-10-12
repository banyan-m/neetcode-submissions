class Solution:
    def isValid(self, s: str) -> bool:
        matching = { "}" : "{" , "]" : "[" , ")" :  "(" }

        stack = []
        for b in s:
            if b not in matching:
                stack.append(b)
            
            else: 
                if not stack or stack[-1] != matching[b]:
                    return False
                
                stack.pop()

        return stack == []

