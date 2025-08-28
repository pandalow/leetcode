Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
 

#### solution1
你之前的实现有几个典型问题：一是 while i < (m-n+1) 的条件写错了 —— 这是在 for 循环枚举起点时才成立，而你的写法用了 双指针+回退逻辑，所以必须让 i < m，否则会提前退出，漏掉正确答案。二是匹配成功的判断条件应当是 j == n，而不是 j == n-1，否则会在模式串最后一个字符还没比时就返回。三是失配时虽然写了 i = i - j + 1 来回退，但忘了重置 j = 0，导致 needle 的位置错乱。

重点理解：
- 在 for 循环版（无回退逻辑）里，i 代表“起始位置”，只能跑到 m-n+1。
- 在 双指针版（有回退逻辑）里，i 表示“正在比的位置”，需要允许走完整个 haystack，因为回退逻辑会隐式地枚举所有起点。

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        i = 0
        j = 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i-j + 1
                j = 0
            
            if j == n:
                return i-j

        return -1

```