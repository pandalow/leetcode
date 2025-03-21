# 1004. Max Consecutive Ones III

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`*'s in the array if you can flip at most* `k` `0`'s.

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```

**Constraints:**

- `1 <= nums.length <= 105`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

- solution
    
    ```python
    class Solution(object):
        def longestOnes(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
    
            left = 0
            right = 0
            zero_count=0
            ans = 0
    
            while right < len(nums):
                if nums[right] == 0:
                    zero_count+=1
    
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count-=1
                    left+=1
    
                ans = max(ans, right-left+1)
                right+=1
            return ans
    ```
    

实际过程是, 因为有翻转需求, 可以变更为 在多长的滑动窗口中, 可以容忍少于 k 个 0:

- 解释
    
    下面给你演示一个 **基于 `while` 循环的滑动窗口方法**，用来求「最长连续的 1，且允许翻转最多 `k` 个 0」。这是一个常见的题目（LeetCode 1004: *Max Consecutive Ones III*），可以用双指针或滑动窗口的方法来解决。
    
    ---
    
    ## 问题说明
    
    - 给定一个只包含 0 和 1 的数组 `nums`，我们可以 **最多** 将其中的 `k` 个 0 翻转成 1。
    - 找到翻转后，**最长的连续 1** 的长度。
    
    ---
    
    ## 原理讲解
    
    1. 定义两个指针 `left` 和 `right`，初始化都为 0。
    2. 定义 `zero_count` 来统计 **窗口 `[left, right]` 范围内 0 的个数**。
    3. 不断向右移动 `right`：
        - 如果遇到 0，则 `zero_count += 1`。
        - 当 `zero_count > k` 时，说明当前窗口里 0 的数量超过了可翻转的上限，需要移动 `left` 缩小窗口：
            - 如果移除的元素是 0，则 `zero_count -= 1`。
            - `left += 1`，直到 `zero_count <= k`。
    4. 只要保持 `zero_count <= k`，窗口 `[left, right]` 就是**合法窗口**，其长度 `right - left + 1` 就是一个候选答案，记录更新到 `ans` 中。
    
    由于 `left` 和 `right` 各自只会遍历数组一次，所以整体时间复杂度是 `O(n)`。
    
    ---
    
    ## 修正后的代码（While 版本）
    
    ```python
    class Solution(object):
        def longestOnes(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            left = 0
            right = 0
            zero_count = 0  # 记录当前窗口里 0 的个数
            ans = 0
    
            while right < len(nums):
                # 如果当前数字是 0，则计数加 1
                if nums[right] == 0:
                    zero_count += 1
    
                # 当 0 的数量超过 k，移动 left 缩小窗口，直到 zero_count <= k
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
    
                # 此时 [left, right] 内 0 的数量 <= k，是合法窗口
                ans = max(ans, right - left + 1)
    
                right += 1
    
            return ans
    
    ```
    
    ### **为什么这样写就可以？**
    
    - **核心在于维护一个“滑动窗口”**，其中 0 的个数不超过 `k`。
    - 每当 0 的个数超过 `k`，就不断地移动 `left`，并且如果移除的是 0，就让 `zero_count` 减 1。
    - 这样可以保证窗口 `[left, right]` 内始终最多只有 `k` 个 0。
    
    ---
    
    ## 测试样例
    
    ```python
    sol = Solution()
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # 输出: 6
    # 解释：翻转 [0,0] 中的任意两个 0，都可以得到一段最长连续 1，长度为 6。
    
    ```
    
    你也可以自行设计更多用例来测试。本方法广泛应用于「长窗口中可容忍多少个某种元素」的场景，原理非常通用。