class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        
        for m, sublist in enumerate(matrix):

            low, high = 0, len(sublist) - 1

            

            while low <= high:

                mid = (low + high) // 2 

                if target < sublist[mid]:
                    high = mid - 1
                
                elif target > sublist[mid]:
                    low = mid + 1
                
                else: 
                    return True
            
        return False


        