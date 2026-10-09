class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in matching:
                stack.append(c)  # opening bracket
            else:
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()

        return not stack