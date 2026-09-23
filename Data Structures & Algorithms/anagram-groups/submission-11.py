class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      newMap = {}

      for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c)-ord('a')] += 1
        
        key = tuple(count)

        if key in newMap:
            newMap[key].append(s)
        else:
            newMap[key] = [s]

      return list(newMap.values())