import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * len(nums)

        if zeros == 1:
            p = 1
            for x in nums:
                if x != 0:
                    p *= x
            return [p if x == 0 else 0 for x in nums]

        p = 1
        for x in nums:
            p *= x

        return [int(p * x**-1) for x in nums]
        


        
            

        