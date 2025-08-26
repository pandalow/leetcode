# 349. Intersection of Two Arrays

Given two integer arrays `nums1` and `nums2`, return *an array of their*

*intersection*

. Each element in the result must be

**unique**

and you may return the result in

**any order**

.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

- solution
    
    ```python
    class Solution(object):
        def intersection(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            nums1.sort()
            nums2.sort()
    
            left_1 = 0
            left_2 = 0
            digit = []
            while left_1 < len(nums1) and left_2 < len(nums2):
    
                if nums1[left_1] == nums2[left_2]:
                    if nums1[left_1] not in digit:
                        digit.append(nums1[left_1])
                    left_1+=1
                    left_2+=1
                elif nums1[left_1] < nums2[left_2]:
                    left_1 +=1
                else:
                    left_2+=1
    
            return digit
    
                
    ```
    
- Explain
    1. 核心是要排序数组, 这样确保两个指针可以进行有序的递进
        1. 如果1 pointer 小于 2 pointer , 就推进1,
        2. 如果 1 pointer 大于 2 pointer, 就推进2
        3. 逐步推进, 达成遍历两个数组的情况
    2. 最简单的方法其实是用set()
        1. 把两个都进set, 比较是否有相同的值



#### Solution 2 hashmap

本质是第一个创建两个个hashset, 用hashmap的方式, 然后第二个去查一下第一个的重复数字就行了
O(2n)

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hm = {}
        data = []
        hm2 = {}
        for item in nums1:
            if item not in hm:
                hm[item] = item
        
        for item in nums2:
            if item in hm:
                if item not in hm2:
                    hm2[item] = item
                    data.append(item)

        return data
```
