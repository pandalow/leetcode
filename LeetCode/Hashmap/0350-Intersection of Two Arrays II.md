Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


#### Solution 1
1. hashmap计算第一个nums的词频, 如果出现重复就+=1
2. 用第二个nums去查询第一个的hashmap, 如果重复就-=1, 只要大于等于0,就证明这个是多次重复的情况.加入数组

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hm1 = {}
        data = []
        for i in nums1:
            if i not in hm1:
                hm1[i] = 0
            else:
                hm1[i] += 1
        for i in nums2:
            if i in hm1 and hm1[i] >= 0:
                hm1[i] -= 1
                data.append(i)
        
        return data

```


#### Solution 2: Two pointer
1. 用2 pointer更加方便一些, 直接两个指针做上下对比;
2. 如果一致就记录下, 往下走

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        data = []
        
        nums1.sort()
        nums2.sort()

        left1 = 0
        left2 = 0

        while left1 < len(nums1) and left2 < len(nums2):
            l1 = nums1[left1]
            l2 = nums2[left2]

            if l1 == l2:
                data.append(l1)
                left1+=1
                left2+=1
            elif l1 < l2:
                left1+=1
            elif l1 > l2:
                left2+=1
        
        return data

```