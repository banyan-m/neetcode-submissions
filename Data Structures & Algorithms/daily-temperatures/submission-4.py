class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        tStack = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prevTemp, prevDay = stack.pop()
                tStack[prevDay] = i - prevDay
            
            stack.append((t,i))

        
        return tStack


        

        