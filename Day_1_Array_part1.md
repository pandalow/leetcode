### Array

[Binary Search-704](https://leetcode.com/problems/binary-search/description/)
递归法: 
1. 递归终止条件缺失: 注意 left > right 为递归终止条件;
2. len(nums)- 1 为 实际的pointer
3. python 整除法为 //
循环法:
1. `while(left <= right)` 用来检查唯一元素的情况


[Remove Element - 27](https://leetcode.com/problems/remove-element/description/)
暴力破解法:
1. 冒泡排序原来交换元素, 每次遇到对应元素 与 元素+1 index 交换;
2. 使用size来控制整个交换的范围, 最后返回size,即为最终非命中元素的长度;
3. 外层用i控制, 内层用j来控制索引

双指针:
1. fast 指针：负责扫描数组中每一个元素。
2. slow 指针：负责维护“新数组”的末尾。

    流程：
    当 nums[fast] == val 时，跳过这个元素（fast += 1），相当于删除。
    当 nums[fast] != val 时，把这个元素写到 nums[slow]，再同时 slow += 1。
    最后 slow 就是新数组的长度。


[Squares of a Sorted Array 977](https://leetcode.com/problems/squares-of-a-sorted-array/description/)
暴力破解:
1. 先集体平方后, 再直接快排

双指针:
1. 核心的规律是平方两端必然是排序最后的值, 无论+/-的绝对值平方都很大;
2. 所以只要用指针比较双端的值, 从而确认谁排再后面就可以了
3. 用第三个指针来指向一个新的数组, 从而插入, 每次-=1