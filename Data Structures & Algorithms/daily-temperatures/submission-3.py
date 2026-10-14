class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        tempStack = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev_temp, prev_day = stack.pop()
                tempStack[prev_day] = i - prev_day

            stack.append((t,i))

        return tempStack

        

        