class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nMap = {}

        for n in nums:
            nMap[n] = nMap.get(n,0) + 1

        
        pairs = []

        for n, f in nMap.items():
            pairs.append((f,n))
        
        pairs.sort(reverse=True)

        res = []

        for f, n in pairs[:k]:
            res.append(n)
        
        return res







        
       


        
       
        