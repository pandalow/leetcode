[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

```
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0: return 0
        #用lambda函数排序
        points.sort(key=lambda x: x[0])
        res = 1
        for i in range(1, len(points)):
            # 左边界和上一个气球右边界是否重叠
            if points[i][0] > points[i-1][1]:
                res += 1
            else:
                # 取最小右边界，下一轮去对比
                points[i][1] =  min(points[i-1][1], points[i][1])

        return res
```

1. 如果气球重叠了，重叠气球中右边边界的最小值 之前的区间一定需要一个弓箭。


[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0: return 0
        #核心思路依然是重叠区间
        count = 0
    
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            # 左边界
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            else:
                count+=1
                #依然取最小值， 因为依然必然重叠
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return count
```