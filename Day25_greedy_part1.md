贪心的本质是选择每一阶段的局部最优，从而达到全局最优。
* 将问题分解为若干个子问题
* 找出适合的贪心策略
* 求解每一个子问题的最优解
* 将局部最优解堆叠成全局最优解


[455. Assign Cookies](https://leetcode.com/problems/assign-cookies/submissions/1804232325/)
暴力破解 超时了
```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        # 需要进行排序
        g.sort()
        s.sort()
        
        for i in range(len(s)):
            # 局部最优, 即为正好s[i] 和 g[j] 相等或者时满足s的最小值 min (s[i] - g[j])
            mini = float('inf')
            min_idx = -1
            for j in range(len(g)):
                if s[i]-g[j]>=0:
                    mini = min(mini, s[i]-g[j])
                    min_idx = j
            #remove s[idx]
            if min_idx >= 0:
                g.pop(min_idx)
                count+=1

        return count
```

正解:

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        j = len(s) - 1  # 从最大饼干开始
        #从最大胃口的孩子开始
        for i in range(len(g) - 1, -1, -1): 
            if j >= 0 and s[j] >= g[i]:
                count += 1
                j -= 1  # 这块饼干用掉
        return count
```
1. 从胃口最大的孩子开始，用当前能满足他的最大饼干去喂。
正向双指针	从小到大	小饼干先喂小胃口	O(n log n)
反向双指针 ✅	从大到小	大饼干喂大胃口	O(n log n)

