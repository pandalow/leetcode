
[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)
1. 如何确定可以用滑动窗口:
    * 题目涉及“连续的子数组/子串”吗？
        * 问题通常限制在数组或字符串的连续片段，而不是任意子集。
    * 是否能通过扩展和收缩来维持某种约束？
        * 需要一个窗口去扩展（右边加元素），在满足某个条件时收缩（左边去元素）。
窗口左右指针只往前走，不会回退 → O(n) 时间复杂度。
2. 重点为确定如何移动滑动窗口的启示位置
    * 该题中使用的是满足target条件时, 就可以缩小窗口, 即移动启动位置.
3. 窗口值随着left的移动还会变化, 又可能出现 >= target的情况


[59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

1. 模拟题目: 左闭右开的方式完成
2. 循环控制, n // 2 , 
    * 每跑完一圈，矩阵的可用边界向里缩一格, 等价于行和列的 有效长度同时减少 2。
    * 每次缩小 2 → 能缩的次数就是矩阵边长除以 2。
    * 就等于 一个边长 n 能被减掉 2 几次
3. offset, 控制边界收缩的变量
    * 上循环: offset 决定右边界。
    * 右循环: offset 决定下边界。
    * 下循环: offset 控制左端点停在哪里。
    * 左循环: offset 控制上端点停在哪里。

[区间和](https://programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC)
1. 在以下问题时可以快速求解:
    * 很多时候题目会问：
    * 子数组的和是多少？
    * 某区间 [i, j] 的和是多少？
    * 有没有子数组的和等于 K？
    * 最大/最小子数组和是多少？
2. 前缀和数组 `prefix[i]` 表示： 从数组起点到下标 i 的所有元素之和
3. `prefix[i]` 表示 前 i 个元素的和。所以 prefix 的下标比 nums 往后移了一位。
4. 用累积和把「多次区间求和」问题转化为「两个数相减」。

```python
import sys

def main():
    size = int(input())

    nums = [int(input()) for _ in range(size)]

    prefix = [0] * (size + 1)
    for i in range(1, size+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    for line in sys.stdin:
        l, r = map(int, line.split())
        print(prefix[r+1] - prefix[l])
    


if __name__ == '__main__':

    main()
```