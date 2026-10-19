class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        fleet = 0
        pair = []
        tempS = []

        for i, s in enumerate(speed):
            time = (target - position[i]) / s
            tempS.append(time)
            pair.append((position[i], time))

        pair.sort(reverse=True)

            
        stack = []

        for position, time in pair:
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
            

