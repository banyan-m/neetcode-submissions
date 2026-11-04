class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()

        k = len(piles) - 1
        k = piles[k]
        o = 1
        res = k

        while o <= k:

            mid = (k + o) // 2

            total = 0 
            for b in piles:
                total += math.ceil(float(b)/mid)

            if total <= h:
                res = mid
                k = mid - 1
            else:
                o = mid + 1
                
        return res
                    














        


        