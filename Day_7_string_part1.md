[344. Reverse String](https://leetcode.com/problems/reverse-string/description/)
1. 双指针就可以解决, 只要swap两个字符的位置

[541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
1. 👉 从左到右，每 2k 一段，只反转前 k 个字符。
2. 在最后一组时，因为可能不足 2k 才需要单独解释。
    * 每次处理 [left : left + 2k) 这一段，翻转其中 [left : left + k)。
    * 如果剩下的长度不足 2k，就要看看是 < k 还是 [k, 2k)，这时才用到那两个规则。

[54. Replace numbers](https://kamacoder.com/problempage.php?pid=1064)

1. 数组填充类的问题，其做法都是先预先给数组扩容带填充后的大小，然后在从后向前进行操作。