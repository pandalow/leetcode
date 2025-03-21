# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array of integers `arr` and two integers `k` and `threshold`, return *the number of sub-arrays of size* `k` *and average greater than or equal to* `threshold`.

**Example 1:**

```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

```

**Example 2:**

```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

```

- solution
    
    ```python
    class Solution(object):
        def numOfSubarrays(self, arr, k, threshold):
            """
            :type arr: List[int]
            :type k: int
            :type threshold: int
            :rtype: int
            """
    
            left = 0
            right = 0
            window = 0
    
            count = 0 
            while right < len(arr):
                window += arr[right]
    
                if right - left + 1 >= k:
                    if window/k >= threshold:
                        count+=1
    
                    window -= arr[left]
                    left +=1
                right +=1
    
            return count
    ```
    
- explain
    - 滑动窗口不一定是一个数组, 可以在范围内维护一个值, 对这个值假想是和或乘积
    - 当右移时加上后面的值, 减少左边的值
    - 固定滑动窗口:
        - 管理一个窗口, 不断添加右边的数值, 直到满足条件, 同时删除左边的数值