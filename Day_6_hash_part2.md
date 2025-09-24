[454. 4Sum II](https://leetcode.com/problems/4sum-ii/description/)
1. 把 **前两数组的和 (a+b)** 全部统计到哈希表，记录“和 → 出现次数”。
2. 遍历 **后两数组的和 (c+d)**，计算目标 `target = -(c+d)`。
3. 如果 `target` 在哈希表里，说明存在 `(a+b) + (c+d) = 0`，直接把次数 `map[target]` 累加到结果。
4. `map[target]` 本身就是多种 (a+b) 组合的数量，所以一次加上即可，不会漏情况。

本质：**用哈希表提前记住一半的组合，再用另一半去匹配，四重循环降为两次双循环。**



[383. Ransom Note](https://leetcode.com/problems/ransom-note/description/)

1. 采用空间换取时间的哈希策略

[15. 3Sum](https://leetcode.com/problems/3sum/description/)

1. 去重逻辑相对复杂, 需要考虑 nums[i] == nums[i-1] , 是避免跳过+1 为相同的情况, 而去除过出现的三元组
2. 双指针原理上是i, left 和 right 互相移动.
3. 但双指针的一个有效前提是需要有序数组, 并不返回真实索引值. 这样不会因为排序引起的干扰造成数据失真.


