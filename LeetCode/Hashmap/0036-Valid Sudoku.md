Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

#### Solution
The Core Concept is :
1.  Using 3 of 2 dimision arrays+set/dict to store the seen data
2. Using x//2 * 3 + y//3 to locate the box locating the box index. 

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row = [dict() for _ in range(len(board))]
        col = [dict() for _ in range(len(board))]
        box = [dict() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c == ".":
                    continue
    
                if c in row[i]: return False
                row[i][c] = c
    
                if c in col[j]: return False
                col[j][c] = c
    
                indice = (i//3 *3) + j//3 
    
                if c in box[indice]: return False
                box[indice][c] = c

        return True
```