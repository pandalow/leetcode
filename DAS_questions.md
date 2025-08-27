


### Hashmap
[706](LeetCode/Hashmap/0706_Design_HashMap.md)

1. 分离链接（chaining）：数组 + 桶（最常见，也最直观）。
2. 开放寻址（open addressing）：如果冲突，就往后找下一个空位（如线性探测、二次探测、双重哈希）。
3. 再哈希（rehashing）：换一个新的哈希函数，直到不冲突（效率差）。

### String

1. 字符串匹配问题
2. 子串相关问题
3. 前缀/后缀相关问题
4. 回文串相关问题
5. 子序列相关问题


**「反转字符串 / 数组」其实是经典的 对称性问题：我要操作的目标是 一头一尾 吗？

** 如果答案是 Yes，那基本上就是对撞指针的套路。

[125](LeetCode/Two_pointer/125_Valid_Palindrome.md)  |  [344](LeetCode/Two_pointer/344_Reverse_String.md)

** 特殊的翻转, 切词起手

[557](LeetCode/String/557_Reverse_Words_in_a_String_III.md)