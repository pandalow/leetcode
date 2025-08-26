
#### Hashmap
[706](leetcode/LeetCode/Hashmap/0706_Design_HashMap.md)

1. 分离链接（chaining）：数组 + 桶（最常见，也最直观）。
2. 开放寻址（open addressing）：如果冲突，就往后找下一个空位（如线性探测、二次探测、双重哈希）。
3. 再哈希（rehashing）：换一个新的哈希函数，直到不冲突（效率差）。