
[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] >=0:
                res += prices[i]- prices[i-1]

        return res
```
1. 拆解收集为每天的利润的和， 有正有负， 只要收集正数(局部最优)
2. 系统性解法为动态规划
    * 此时就是把利润分解为每天为单位的维度，而不是从 0 天到第 3 天整体去考虑.


[55](55. Jump Game)
```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        cover = 0
        if cover == len(nums)-1: return True
        i = 0
        while i<=cover:
            # 最大覆盖范围与当前最大覆盖范围
            cover = max(i+nums[i], cover)
            if cover >= len(nums) - 1 : return True
            i+=1
        
        return False
```
1. 换一思路， 只去看覆盖范围，只要覆盖范围范围到了终点位置，就是算可以跳到了

[1005. Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)
```python
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = k
        for i in range(len(nums)):
            if nums[i] < 0 and count> 0:
                nums[i] = - nums[i]
                count-=1
        # 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        if count % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
        
        return sum(nums)
```