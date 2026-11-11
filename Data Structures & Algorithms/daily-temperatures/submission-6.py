class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        tStack = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                tStack[ind] = i - ind
            
            stack.append((t,i))
        
        return tStack



        

        