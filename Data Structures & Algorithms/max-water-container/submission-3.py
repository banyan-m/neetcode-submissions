class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        volume = 0

        while l < r:
            side = min(heights[l], heights[r])
            bottom = r - l
            v = side * bottom 
            volume = max(v,volume)

            if heights[l] < heights[r] and l < r:
                l += 1
                
            elif heights[l] >= heights[r] and l < r:
                r -= 1
            
        
        return volume



            

        