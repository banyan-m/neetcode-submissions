class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kMap = {}

        for n in nums:
            kMap[n] = kMap.get(n,0) + 1

        
        pairs = []
        for value, freq in kMap.items():
            pairs.append((freq,value))

        pairs.sort(reverse=True)

        result = []
        for freq, value in pairs[:k]:
            result.append(value)

        return result



        
       
        