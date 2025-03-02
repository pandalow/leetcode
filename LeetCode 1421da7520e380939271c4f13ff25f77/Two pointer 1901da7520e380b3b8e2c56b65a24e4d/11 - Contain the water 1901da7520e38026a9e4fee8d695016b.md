# 11 - Contain the water

[https://leetcode.com/problems/container-with-most-water/description/](https://leetcode.com/problems/container-with-most-water/description/)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

还没有解决

- solution
    
    ```python
    class Solution(object):
        def maxArea(self, height):
            """
            :type height: List[int]
            :rtype: int
            """
            
            left = 0
            right = len(height)-1
            ans = 0
            while left < right:
                area = min(height[left],height[right]) * (right-left)
                ans = max(area,ans)
                if height[left] < height[right]:
                    left+=1
                else:
                    right-=1
                
    
            return ans
    ```
    
- explain
    
    核心是对装水的面积逻辑研究:
    
    容纳的水量是由「左右两端直线中较低直线的高度 * 两端直线之间的距离」所决定的。所以我们应该使得「」，这样才能使盛水面积尽可能的大。
    
    可以使用对撞指针求解。移动较低直线所在的指针位置，从而得到不同的高度和面积，最终获取其中最大的面积