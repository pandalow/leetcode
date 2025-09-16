


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


### Tree
[144](https://leetcode.com/problems/binary-tree-preorder-traversal/)
[94](https://leetcode.com/problems/binary-tree-inorder-traversal/)
[145](https://leetcode.com/problems/binary-tree-postorder-traversal/)
[102](https://leetcode.com/problems/binary-tree-level-order-traversal/)

#### Recursion
[104](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/);
[递归3步](LeetCode/递归3步.md)
[112](https://leetcode.com/problems/path-sum/description/)


### BST
[700](https://leetcode.com/problems/search-in-a-binary-search-tree/)
[701](https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1771680311/)
所有的插入操作都会将该结点放入BST中的叶子结点, 从不进行重新的安排操作
[450](https://leetcode.com/problems/delete-node-in-a-bst/description/)
三种情况,
1. 无叶子结点, 返回null
2. 有左/右叶子结点, 直接返回下一个左结点,右结点
3. 两边都有, 找到右边最小值, 复制到当前结点, 删除最小值.自然成立.(因为右边最小值必然比左边都大,又右边的其他值都笑, 不需要调整结点顺序,就可以承担当前结点功能)

https://www.youtube.com/watch?v=wcIRPqTR3Kc&t=2s

[98](https://leetcode.com/problems/validate-binary-search-tree/description/)