# 724. Find Pivot Index

- Question
    
    Given an array of integers `nums`, calculate the **pivot index** of this array.
    
    The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.
    
    If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.
    
    Return *the **leftmost pivot index***. If no such index exists, return `-1`.
    
    **Example 1:**
    
    ```
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
    
    ```
    
    **Example 2:**
    
    ```
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.
    ```
    
    **Example 3:**
    
    ```
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
    
    ```
    
    **Constraints:**
    
    - `1 <= nums.length <= 104`
    - `1000 <= nums[i] <= 1000`

My solution

```python

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sums = 0
        idx = -1
        for i in range(len(nums)):
            left_sums += nums[i]
            if(left_sums == (total-(left_sums-nums[i]))):
                idx = i
                break
        
        return idx
        
```

- 我这个核心是直接找到除去当前索引值外, 前面加和正好等于`total`减去左边(即右边剩下的值)的情况, 如果出现, 就break并存入idx

Official solution

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in nums:
            total += i

        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum * 2 - nums[i] == total:
                return i

        return -1
        

```

- 这里换了判断条件, 左边*2 - 多余加过的一次中间值