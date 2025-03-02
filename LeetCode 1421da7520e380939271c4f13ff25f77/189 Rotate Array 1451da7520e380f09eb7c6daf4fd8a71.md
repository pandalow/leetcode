# 189. Rotate Array

- Question
    
    Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
    
    **Example 1:**
    
    ```
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    
    ```
    
    **Example 2:**
    
    ```
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    
    ```
    
    **Constraints:**
    
    - `1 <= nums.length <= 105`
    - `231 <= nums[i] <= 231 - 1`
    - `0 <= k <= 105`

Solution

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(self,nums,left,right):
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
                
            return nums

        nums = reverse(self,nums,0,len(nums)-1)
        nums = reverse(self,nums,0,k-1)
        nums = reverse(self,nums,k,len(nums)-1)    

        return nums
```

- 核心是reverse这个方法的三次翻转
    - 首次将数组倒置, 变成逆序
    - 第二次将0 到 k的值翻转, 就会获得一个翻转的正序插入
    - 第三次将k值之后的值再做一次翻转, 就会获得后面的值插入前面的效果
-