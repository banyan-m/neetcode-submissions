class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        tHash = {}
        sHash = {}

        for i in s:
            sHash[i] = sHash.get(i, 0) + 1
            
        for i in t:
            tHash[i] = tHash.get(i, 0) + 1
            
        return sHash == tHash