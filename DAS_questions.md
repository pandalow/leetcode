


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


#### BF 算法
最坏情况是每一趟比较都在模式串的最后遇到了字符不匹配的情况，每轮比较需要进行 m 次字符对比，总共需要进行 n-m+1 轮比较，总的比较次数为 m * (n-m+1)。所以 BF 算法的最坏时间复杂度为 m * n。

[28](LeetCode/String/28_Find_the_Index_of_the_First_Occurrence in a String.md)
[796](LeetCode/String/796_Rotate_String.md)


#### KMP算法
https://www.youtube.com/watch?v=V5-7GzOfADQ
[459](LeetCode/String/459_Repeated_Substring_Pattern.md)

#### 字典树

[208](LeetCode/String/208_Implement_Trie_(Prefix_Tree).md)