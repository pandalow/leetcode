# 674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers `nums`, return *the length of the longest **continuous increasing subsequence** (i.e. subarray)*. The subsequence must be **strictly** increasing.

A **continuous increasing subsequence** is defined by two indices `l` and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

**Example 1:**

```
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.

```

**Example 2:**

```
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
```

- solution
    
    ```python
    class Solution(object):
        def findLengthOfLCIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            right = 0
            window_size = 0
            ans= 0
    
            while right < len(nums):
                window_size += 1
    
                if nums[right] <= nums[right-1] and right>0:
                    window_size=1
                
                ans = max(window_size, ans)
                right+=1
                
            return ans
    ```
    

下面我们来分析你的代码，并给出一个修正后的 **while 循环版本**，用于求 **数组 `nums` 中的最长连续递增子序列**（LCIS, *Longest Continuous Increasing Subsequence*）。

---

## 1. 你原始代码存在的问题

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        left = 0
        right = 0
        window_size = 0
        ans = 0

        while right < len(nums):
            window_size += 1

            if nums[right] > nums[right-1]:
                left = right
                window_size = 1

            ans = max(window_size, ans)
            right += 1

        return ans

```

1. **`nums[right-1]` 在 `right = 0` 时会越界**
    
    当 `right = 0` 时，你访问 `nums[right-1]` 实际上是 `nums[-1]`，会出问题或逻辑出错。
    
2. **逻辑与“递增”相反**
    - 代码里：
    
    这句话的意思是：一旦发现「递增」，就 **重置** `window_size` 为 1——这与我们想要的“遇到递增就把子序列长度加 1”恰好相反。
        
        ```python
        if nums[right] > nums[right-1]:
            left = right
            window_size = 1
        
        ```
        
    - 正确逻辑应该是：**如果当前元素 `nums[right]` 比前一个元素 `nums[right-1]` 大，就继续增加长度；否则就重置。**
3. **初始化问题**
    - 你在循环开始时 `window_size = 0`，每次都 `window_size += 1`，但是第一次循环就需要小心处理；并且还要注意在第一个元素时无法对比 `nums[right-1]`。

---

## 2. 正确的思路

- 如果 `nums[i] > nums[i-1]`，说明子序列还在继续增长，因此 `当前连续递增长度 += 1`。
- 如果 `nums[i] <= nums[i-1]`，则需要 **重置** 连续递增长度为 1（从 `nums[i]` 本身重新开始计数）。
- 在每一步都更新 `ans = max(ans, 当前连续递增长度)`。

这在更常见的 **for 循环** 写法中，通常是：

```python
def findLengthOfLCIS(nums):
    if not nums:
        return 0

    ans = 1
    current_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_len += 1
        else:
            current_len = 1
        ans = max(ans, current_len)

    return ans

```

但你明确希望使用 **while 循环**，我们就把它写成 while 的形式。

---

## 3. 修正后的 **while** 写法

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # 如果 nums 为空，直接返回 0

        ans = 1                 # 全局最长连续递增子序列的长度
        current_len = 1         # 当前这段递增子序列的长度

        right = 1  # 从下标 1 开始，对比 nums[right] 和 nums[right-1]
        while right < len(nums):
            if nums[right] > nums[right - 1]:
                current_len += 1
            else:
                current_len = 1  # 重新开始递增计数

            ans = max(ans, current_len)
            right += 1

        return ans

```

### **代码说明**

1. **特判空数组**：若 `nums` 为空，直接返回 0。
2. **初始化**：
    - `ans = 1`：因为只要数组不空，最短的 LCIS 至少是 1（单个元素）。
    - `current_len = 1`：以第一个元素开局。
    - `right = 1`：从第二个元素（下标 1）开始对比。
3. **主循环（while）**：
    - 若 `nums[right] > nums[right-1]`，说明还在递增区间，`current_len += 1`。
    - 否则不再递增，`current_len = 1` 重置长度为 1。
    - 每次更新 `ans = max(ans, current_len)`。
4. **返回 `ans`**。

这样就能保证：

- **遇到递增，就累加**；
- **遇到不增，就重置**；
- 同时使用 **while** 循环，而不越界。

---

## 4. 复杂度分析

- **时间复杂度**：`O(n)`，其中 `n = len(nums)`。因为我们只用一个指针 `right` 线性遍历一次数组。
- **空间复杂度**：`O(1)`，只使用了常量额外空间。

---

## 5. 测试

- **示例 1**
    
    ```python
    nums = [1, 3, 5, 4, 7]
    # 最长连续递增子序列是 [1, 3, 5] 或者 [3, 5]、[5, 4, 7] 需要判断
    # 实际上 [1, 3, 5] 长度为 3，遇到 5 -> 4 不增，重置。
    # 再从 4 -> 7 递增，长度 2。
    # 最终答案为 3。
    print(sol.findLengthOfLCIS(nums))  # 3
    
    ```
    
- **示例 2**
    
    ```python
    nums = [2, 2, 2, 2]
    # 全部元素相等，没有严格递增的相邻元素，所以最长连续递增子序列长度是 1
    print(sol.findLengthOfLCIS(nums))  # 1
    
    ```
    
- **示例 3**
    
    ```python
    nums = [1, 2, 3, 4, 5]
    # 整个数组都是递增的，长度是 5
    print(sol.findLengthOfLCIS(nums))  # 5
    
    ```
    

通过以上示例就能验证结果是否正确。

---

### **结论**

- 关键是：当发现 `nums[i] > nums[i-1]` 时，说明可以扩大当前的递增子序列；否则就重置。
- 你的原始代码恰好把逻辑写反了，并且没有处理 `right=0` 时的边界情况。
- 按上述修正的 **while** 循环版本即可得到正确的 **最长连续递增子序列** 长度。