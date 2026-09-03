class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for l in s:
            sMap[l] = 1 + sMap.get(l, 0)
        
        for l in t:
            tMap[l] = 1 + tMap.get(l, 0)
        
        if sMap == tMap:
            return True 

        else:
            return False

