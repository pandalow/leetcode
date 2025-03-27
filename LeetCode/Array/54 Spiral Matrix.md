# 54. Spiral Matrix

- Question
    
    Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.
    
    **Example 1:**
    
    ![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
    
    ```
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    
    ```
    
    **Example 2:**
    
    ![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
    
    ```
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    
    ```
    
    **Constraints:**
    
    - `m == matrix.length`
    - `n == matrix[i].length`
    - `1 <= m, n <= 10`
    - `100 <= matrix[i][j] <= 100`

Notes: 在研究研究的

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # [i][j] -> [i][j+1] -> [i][j+2] 
        # ->[i+1][j+2] -> [i+2][j+2] -> [i+2][j+1] 
        # ->[i+2][j] ->[i+1][j] -> [i+1][j+1]

        up, down, left, right = 0,len(matrix)-1,0,len(matrix[0])-1

        ans = []

        while(True):
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up+=1
            if up > down:
                break
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right-=1
            if right < left:
                break
            for i in range(right, left-1,-1):
                ans.append(matrix[down][i])
            down -=1
            if up > down:
                break
            for i in range(down, up-1,-1):
                ans.append(matrix[i][left])
            left+=1
            if left >right:
                break
            
        return ans
        
```