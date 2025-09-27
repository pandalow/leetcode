[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

1. 和计算器的方式比较一致， 主要是理解stack，stack的堆叠方式和这个表达式契合：
2. 每一次的优先计算结果会被压入stack， 然后取出前一次计算结果进行进一步计算。
3. 理论最后一次必然为一个符号， 所以results_list最后必然只剩一个数字， 为最终结果。


[239](https://leetcode.com/problems/sliding-window-maximum/)

1. 单调队列的方案：始终维护deque队列为左大右边小， 同时符合窗口设置， 这样自然就可以处理了，
2. dq 维护的是下标而不是实际的数字

```python

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # 存下标，保持单调递减
        res = []

        for i, num in enumerate(nums):
            # 保持单调递减：移除比当前小的
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            # 移除窗口外的元素
            if dq[0] <= i - k:
                dq.popleft()

            # 形成一个完整窗口后，记录最大值
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res
```