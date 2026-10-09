class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsMap = {}

        for n in nums:
            if n in numsMap:
                return True
            
            numsMap[n] =+ 1
        
        return False