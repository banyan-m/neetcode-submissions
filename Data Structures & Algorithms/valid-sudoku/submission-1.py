class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        boxMap = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                val = board[r][c]
                if val == ".":
                    continue

                box = (r //3) * 3 + (c // 3)


                if val in rowMap[r] or val in  colMap[c] or val in boxMap[box]:
                    return False
                rowMap[r].add(val)
                colMap[c].add(val)
                boxMap[box].add(val)
        
        return True