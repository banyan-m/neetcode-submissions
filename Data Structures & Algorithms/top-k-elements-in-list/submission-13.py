class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        topMap = {}
        pairs = []
        result = [] 

        for n in nums:
            topMap[n] = topMap.get(n,0) + 1

        for n, c in topMap.items():
            pairs.append([c,n])

        pairs.sort(reverse=True)
        
        for c , n in pairs[:k]:
            result.append(n)
        
        return result


        
        
       


        
       
        