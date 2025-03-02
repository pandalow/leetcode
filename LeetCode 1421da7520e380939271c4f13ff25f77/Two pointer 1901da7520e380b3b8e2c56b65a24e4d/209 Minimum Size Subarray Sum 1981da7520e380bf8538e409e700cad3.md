# 209. Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a*

*subarray*

*whose sum is greater than or equal to*

```
target
```

. If there is no such subarray, return

```
0
```

instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

**Constraints:**

- `1 <= target <= 109`
- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`

**Follow up:**

If you have figured out the

```
O(n)
```

solution, try coding another solution of which the time complexity is

```
O(n log(n))
```

.

- solution
    
    ```python
    class Solution(object):
        def minSubArrayLen(self, target, nums):
            """
            :type target: int
            :type nums: List[int]
            :rtype: int
            """
            left = 0
            right = 0
            ans = float('inf')
            sums = 0
    
            while right < len(nums):
                sums += nums[right]
    
                while sums >= target:
                    ans = min(ans, right-left+1)
                    sums-=nums[left]
                    left+=1
    
                right += 1
    
            return ans if ans != float('inf') else 0
                
    ```
    
- explain
    
    将最小值的管理放在while中, 最后的return要管理判断是否没有进行left的加减
    
    - 如果sums一直小于target, 则不进入窗口, 那么ans 一直为最大值
    - 所以要确认归零