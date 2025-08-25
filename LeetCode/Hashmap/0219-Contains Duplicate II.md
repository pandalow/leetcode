Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

#### Solution 1
阅读题的时候有问题:
1. 目要求的是 相同元素的索引差是否 ≤ k，不是元素值的差。
2. 反相索引值和key

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i-seen[nums[i]])<=k:
                    return True
            
            seen[nums[i]] = i

        return False
                
```