# *498. Diagonal Traverse

- Question
    
    Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.
    
    **Example 1:**
    
    ![](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)
    
    ```
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    
    ```
    
    **Example 2:**
    
    ```
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]
    
    ```
    
    **Constraints:**
    
    - `m == mat.length`
    - `n == mat[i].length`
    - `1 <= m, n <= 104`
    - `1 <= m * n <= 104`
    - `105 <= mat[i][j] <= 105`

```python
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        m,n= len(mat),len(mat[0])
        x,y = 0,0
        ans = []

        for _ in range(m*n):

            ans.append(mat[x][y])

            if ((x+y)%2==0):
                # 这里有一个细节, 需要先判断列, 再判断行, 因为右上角是列优先的
                if(y==n-1):
                    x+=1
                elif(x==0): 
                    y+=1
                else:
                    x-=1
                    y+=1
            elif((x+y)%2==1):
                if(x==m-1):
                    y+=1
                elif(y==0):
                    x+=1
                else:
                    x+=1
                    y-=1
        return ans
```

Notes:

1. 核心发现右上行走和左下行走 i , j (行, 列) 的规律, 即:
    1. i + j 为偶数是在右上行走
    2. i +j 为奇数是在左下行走
2. 除了行走规律外, 对于边界条件处理很重要:
    1. 用顺序解决了先判断列还是行的问题