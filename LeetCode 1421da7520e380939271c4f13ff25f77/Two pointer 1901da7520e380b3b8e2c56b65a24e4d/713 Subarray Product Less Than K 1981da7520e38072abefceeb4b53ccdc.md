# 713. Subarray Product Less Than K

Given an array of integers `nums` and an integer `k`, return *the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than* `k`.

**Example 1:**

```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

```

**Example 2:**

```
Input: nums = [1,2,3], k = 0
Output: 0

```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 106`

- solution
    
    ```python
    class Solution(object):
        def numSubarrayProductLessThanK(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            if k<=1:
                return 0
            count = 0 
            left = 0
            right = 0
            products = 1
        
    
            while right < len(nums):
                products *= nums[right]
       
                while products >= k:
    
                    products/= nums[left]
                    left+=1             
    
                
                count+=(right-left+1)
                right+=1
            
            return count
    ```
    
- explain
    
    最后的返回时以right为终点, 以left为起点 内的所有数组组合?
    
    是的，`count += (right - left + 1)` 计算的是 **所有以 `right` 结尾的子数组**，这些子数组的 **起点** 可以是 `left` 到 `right` 之间的任意位置。
    
    ---
    
    ## **详细拆解**
    
    对于当前窗口 `[left, right]`，其子数组的 **所有可能组合** 如下：
    
    ```
    nums[left], nums[left+1], ..., nums[right]
    
    ```
    
    所有这些 **以 `right` 结尾** 的子数组包括：
    
    1. `[right]`
    2. `[right-1, right]`
    3. `[right-2, ..., right]`
    4. `...`
    5. `[left, ..., right]`
    
    这些子数组的数量刚好等于窗口的大小 `right - left + 1`。
    
    ---
    
    ## **举例分析**
    
    假设 `nums = [10, 5, 2, 6]`, `k = 100`。
    
    我们遍历 `nums` 并计算 `count`：
    
    | Step | `left` | `right` | Window (`nums[left:right+1]`) | Product | New Subarrays (Count) | Total Count |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 0 | 0 | `[10]` | 10 | 1 ( `[10]` ) | 1 |
    | 2 | 0 | 1 | `[10, 5]` | 50 | 2 ( `[5]`, `[10,5]` ) | 3 |
    | 3 | 0 | 2 | `[10, 5, 2]` | 100 | **窗口缩小** ( `left+=1` ) | - |
    | 3.1 | 1 | 2 | `[5, 2]` | 10 | 2 ( `[2]`, `[5,2]` ) | 5 |
    | 4 | 1 | 3 | `[5, 2, 6]` | 60 | 3 ( `[6]`, `[2,6]`, `[5,2,6]` ) | 8 |
    
    最终答案是 `8`，因为符合 `product < k` 的子数组共有 8 个：
    
    ```
    [10], [5], [10,5], [2], [5,2], [6], [2,6], [5,2,6]
    
    ```
    
    ---
    
    ## **直观理解**
    
    在 `count += (right - left + 1)` 中：
    
    - `right` 表示当前扩展的窗口的 **终点**。
    - `left` 是窗口的 **起点**，它会随着 `product` 变大而向右移动。
    - `right - left + 1` 计算的是 **以 `right` 结尾**，且起点在 `[left, ..., right]` 之间的所有子数组的个数。
    
    ---
    
    ## **总结**
    
    ✅ **每次扩展 `right`，增加了 `right - left + 1` 个新子数组**。
    
    ✅ **所有新增的子数组都必须以 `right` 结尾，且起点可以在 `[left, ..., right]` 之间**。
    
    ✅ **时间复杂度 `O(n)`，因为 `left` 和 `right` 最多各遍历 `nums` 一次**。
    
    这就是 **滑动窗口技巧** 在 **统计子数组个数** 方面的核心思想！🚀