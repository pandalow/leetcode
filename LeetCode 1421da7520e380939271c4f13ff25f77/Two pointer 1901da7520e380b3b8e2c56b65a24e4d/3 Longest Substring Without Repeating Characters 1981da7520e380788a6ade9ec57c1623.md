# 3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest**

**substring**

without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

- solution
    
    ```python
    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            
            left = 0 
            right = 0
            window = {}
            s = list(s)
            ans = 0
            while right < len(s):
                if s[right] not in window:
                    window[s[right]] = 1
                else:
                    window[s[right]] += 1
    
                while window[s[right]]>1:
                    window[s[left]]-=1
                    left+=1
                ans = max(ans,right-left+1)
                right+=1
            
            return ans
    ```
    
- explain
    
    用一个词典来记录维护重复的字符数, 让s[left]和s[right]来访问一个索引,
    
    查询索引数字, 大于1就开始减少s[left]的情况, 直到s[left]能够将s[right]的字符降低至1
    
    - 这就代表了该词组删除到了一个合适的程度
    - 
    
    ![image.png](3%20Longest%20Substring%20Without%20Repeating%20Characters%201981da7520e380788a6ade9ec57c1623/image.png)