# 13. Roman to Integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
SymbolValue
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

- solution
    
    ```python
    class Solution(object):
        def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            vocab = {
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
            }
            count = 0
            idx = 0
            while idx < len(s):
                left_int = vocab[s[idx]]
    
                if idx+1 < len(s):
                    right_int = vocab[s[idx+1]]
                    if s[idx+1] in vocab.keys() and right_int > left_int:
                        count += right_int - left_int
                        idx+=2
                        continue
                count+= vocab[s[idx]]
                idx+=1
    
            return count
    ```
    

1. 核心是一个hashmap去管理字典, 来进行数据查询
2. 循环中 通过 i 和 i+1的限制条件来进行两个指针的控制
    1. 命中条件, 跳过当前字符或者元素(包括i和i+1)
    2. 未命中, 对当前元素进行计算