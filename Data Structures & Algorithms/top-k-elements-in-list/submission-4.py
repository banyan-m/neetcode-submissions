class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kMap = {}
        pairs = []
        res = []

        for n in nums:
            kMap[n] = kMap.get(n,0) + 1

        

        for n, f in kMap.items():
            pairs.append((f,n))
        
        pairs.sort(reverse=True)

        
        for f, n in pairs[:k]:
            res.append(n)
        
        return res



        


        
       


        
       
        