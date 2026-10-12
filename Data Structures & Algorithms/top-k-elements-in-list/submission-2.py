class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kMap = {}

        for n in nums:
            kMap[n] = kMap.get(n,0) + 1

        
        pairs = []

        for num, freq in kMap.items():
            pairs.append((freq,num))
        
        pairs.sort(reverse=True)

        result = []
        for freq, num in pairs[:k]:
            result.append(num)

        return result






        
       


        
       
        