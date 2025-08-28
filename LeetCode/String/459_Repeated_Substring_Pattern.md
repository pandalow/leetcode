Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 


```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m=len(s)
        lps = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left>0 and s[left] != s[right]:
                left = lps[left-1]
            if s[left] == s[right]:
                left+=1
                lps[right] = left

        return lps[-1] > 0 and m%(m-lps[-1])== 0

```


Explaination
对，这个洞察很对 👍。
这道题（LeetCode 459. Repeated Substring Pattern）要求的是：**整个字符串能不能由某个子串重复多次组成**。

---

## 🔑 两类情况

1. **符合要求**：
   整个字符串完全由某个子串重复构成。

   * `"abab"` → `"ab"` \* 2
   * `"abcabcabcabc"` → `"abc"` \* 4

2. **不符合要求**：
   只是**中间有重复**，但整体不能整除。

   * `"aba"` → 中间 `"a"` 重复，但整体不是某个子串重复
   * `"abcaabca"` → 中间 `"abca"` 出现两次，但最后多了一个 `"a"`，所以不符合

---

## 📌 为什么会出现这种「中间重复但不符合」的情况？

因为题目要求的是 **全局重复**，不是「部分重复」。

* **LPS 数组**（KMP 方法）只看「最长前后缀」
* 只有当 **整个字符串长度能被这个重复单元整除** 时，才是符合的。

---

## ✅ 正确的判断条件（KMP 方法）

设 `n = len(s)`，`lps[-1]` = 最长相等前后缀的长度。

* 如果 `lps[-1] > 0` 且 `n % (n - lps[-1]) == 0` → 返回 True
* 否则 False

---

## 🔄 举例

* `"abab"`

  * `lps = [0,0,1,2]`，最后值 `lps[-1] = 2`
  * `n = 4`，`4 % (4-2) == 0` → ✅ True

* `"aba"`

  * `lps = [0,0,1]`，最后值 `lps[-1] = 1`
  * `n = 3`，`3 % (3-1) != 0` → ❌ False

* `"abcabcabcabc"`

  * `lps[-1] = 9`，`n = 12`
  * `12 % (12-9) == 0` → ✅ True

* `"abcaabca"`

  * `lps[-1] = 4`
  * `n = 8`，`8 % (8-4) == 0` → ✅？
  * 但注意 `"abca" * 2 = "abcaabca"`，这个其实是符合的。

如果是 `"abcaabc"` → `lps[-1]=3, n=7` → `7 % (7-3) != 0` → ❌ 不符合。

---

## 🧠 总结

* **中间出现重复 ≠ 整体由重复子串构成**
* 必须同时满足：

  1. 存在前后缀重复（lps\[-1] > 0）
  2. 长度能整除（n % (n - lps\[-1]) == 0）

---

要不要我给你写一段小脚本，把几个「有中间重复 vs 全局重复」的字符串跑一遍，输出 lps 和判断结果？这样更直观。
