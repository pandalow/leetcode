# 3174. Clear Digits

You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

- Delete the *first* digit and the **closest** **non-digit** character to its *left*.

Return the resulting string after removing all digits.

**Example 1:**

**Input:** s = "abc"

**Output:** "abc"

**Explanation:**

There is no digit in the string.

**Example 2:**

**Input:** s = "cb34"

**Output:** ""

**Explanation:**

First, we apply the operation on `s[2]`, and `s` becomes `"c4"`.

Then we apply the operation on `s[1]`, and `s` becomes `""`.

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters and digits.
- The input is generated such that it is possible to delete all digits.

- solution
    
    ```python
    class Solution(object):
        def clearDigits(self, s):
            """
            :type s: str
            :rtype: str
            """
            # slow = 0
            # s=list(s)
    
            # for quick in range(len(s)):
            #     if s[quick].isdigit():
            #         if slow > 0:
            #             slow-=1
            #     else:
            #         s[slow] = s[quick]
            #         slow +=1
            # return "".join(s[:slow])
    
            re = []
            for char in s:
    
                if char.isdigit():
                    if re:
                        re.pop()
                else:
                    re.append(char)
    
            return ''.join(re)
    ```
    
- explain
    1. 使用双指针模拟堆栈的过程，其实是暴力破解。
        1. slow代表stack的顶部pointer
        2. quick是查询的pointer
        3. 如果出现了digit, 就让栈顶的pointer 退后一格
            1. 其中 slow>0来模拟的是栈空的情况
        4. 如果不是, 就往pointer里一直添加数据
    2. 使用顺序堆栈实现,
        1. 出现digit, 移除上一个加入的数据
        2. 未出现, 加入数据
        3. 确保数据不为空,才能进行移除