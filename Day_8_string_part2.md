[151](https://leetcode.com/problems/reverse-words-in-a-string/)
思路逻辑:
1. 移除多余空格
2. 将整个字符串反转
3. 将每个单词反转

[55 kama](https://kamacoder.com/problempage.php?pid=1065)
用了三次翻转的方法
```python
def run():

    n = int(input())
    s = input()

    s = s[::-1]
    s= s[:k][::-1] + s[k:]
    s = s[:k] + s[k:][::-1]

    return s
    
```

[28]()
1. BF 算法
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        i, j = 0, 0
        while i < n and j < m:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i - j + 1
                j = 0
            
        if j == m:
            return i - j
        else:
            return -1
```

2. [需要之后着重理解KMP](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html#%E6%80%9D%E8%B7%AF)