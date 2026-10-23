class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kMap = {}
        pair = []
        result = []

        for n in nums:
            kMap[n] = kMap.get(n,0) + 1

        
        for n, f in kMap.items():
            pair.append((f,n))
        
        pair.sort(reverse=True)

        for f, n in pair[:k]:
            result.append(n)
        
        return result


        
        
       


        
       
        