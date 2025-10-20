[134. Gas Station](https://leetcode.com/problems/gas-station/description/)
```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """ 

        # 需要关注的油量的净增量（补充-消耗）
        # currSum = 剩余油量 如果 剩余油量为负数，前面的站点起始都无法到达
        currSum = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            currSum+=gas[i]-cost[i]
            total+= gas[i]-cost[i]
            if currSum <0:
                start = i+1
                currSum = 0
        if total < 0: return -1
        return start
```
如果总油量减去总消耗大于等于零那么一定可以跑完一圈，说明 各个站点的加油站 剩油量rest[i]相加一定是大于等于零的。

[135. Candy](https://leetcode.com/problems/candy/)
```python
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n

        # 需要分别考虑
        # 右边 比左边大， 从前往后遍历
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:   
            # 左边比右边大， 从后向前遍历
            # candyVec[i]只有取最大的才能既保持对左边candyVec[i - 1]的糖果多，也比右边candyVec[i + 1]的糖果多。
                candy[i] = max(candy[i+1]+1,candy[i])
        
        return sum(candy)
```


[860. Lemonade Change](https://leetcode.com/problems/lemonade-change/description/)
```python
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five+=1
            
            elif bill == 10:
                five-=1
                if five <0:
                    return False
                ten+=1
            
            else: 
                if ten > 0:
                    ten-=1
                    five-=1
                    if five < 0:
                        return False
                else:
                    five-=3
                    if five < 0:
                        return False

        return True
```

* 典型的 贪心算法（Greedy） 问题。每次优先用大面值钞票去找零，保留更多小面额零钱给后续顾客。


