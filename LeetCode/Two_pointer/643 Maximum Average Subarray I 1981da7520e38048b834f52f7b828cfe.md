# 643. Maximum Average Subarray I

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than `10-5` will be accepted.

**Example 1:**

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

**Example 2:**

```
Input: nums = [5], k = 1
Output: 5.00000

```

**Constraints:**

- `n == nums.length`
- `1 <= k <= n <= 105`
- `104 <= nums[i] <= 104`

- solution
    
    ```python
    class Solution(object):
        def findMaxAverage(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
            sums = 0
            left = 0 
            right = 0
            ans = float('-inf')
    
            while right < len(nums):
                sums += nums[right]
                
                if right-left+1 >= k:
                    ans = max(sums/float(k),ans)
                    sums-=nums[left]
                    left+=1
                
                
                right += 1
    
            return ans
    ```
    
- explain
    
    固定滑动窗口, 维护窗口size == k
    
    在正好达成k时, 计算平均值,
    
    注意要除以float(k),避免整除