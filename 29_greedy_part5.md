[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)
```python
class Solution:
    def merge(self, intervals):
        ans = []
        if len(intervals) == 0:
            return  ans  # 区间集合为空直接返回

        intervals.sort(key=lambda x: x[0])  # 按照区间的左边界进行排序

        ans.append(intervals[0])  # 第一个区间可以直接放入结果集中

        for i in range(1, len(intervals)):
            if  ans[-1][1] >= intervals[i][0]:  # 发现重叠区间
                # 合并区间，只需要更新结果集最后一个区间的右边界，因为根据排序，左边界已经是最小的
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                 ans.append(intervals[i])  # 区间不重叠

        return ans

```



[738. Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/)
```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将整数转换为字符串
        strNum = list(str(n))

        # 从右往左遍历字符串
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                strNum[i - 1] = str(int(strNum[i - 1]) - 1)  # 将前一个字符减1
                # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
                for j in range(i, len(strNum)):
                    strNum[j] = '9'

        # 将列表转换为字符串，并将字符串转换为整数并返回
        return int(''.join(strNum))

```

```python
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        strNum = str(n)
        flag = len(strNum)

        for i in range(len(strNum)-1, 0, -1):
            if strNum[i-1] > strNum[i]:
                flag = i
                # strNum 前面几位 + 当前-1位， 加上i位， 拼接
                strNum = strNum[:i-1] + str(int(strNum[i-1])-1) + strNum[i:]
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]

        return int(strNum)
```