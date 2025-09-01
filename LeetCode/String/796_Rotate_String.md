Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

#### Solution 1 : BF
暴力题解

```python
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        queue = collections.deque()

        for w in s:
            queue.append(w)
        
        for i in range(len(queue)):
            if "".join(queue) ==  goal:
                return True
            
            a = queue.popleft()
            queue.append(a)
        
        return False

```


#### Solution 2:
s+s组成一个长串, 必然就是颠倒一次的结果, 是可以用子串查的

```python
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False
                
        new = s + s
        m = len(new)
        n = len(goal)
        left = 0
        right = 0
        while left < m and right < n :
            if new[left] == goal[right]:
                left+=1
                right+=1
            else:
                left = left - right + 1
                right = 0

            if right == len(goal):
                return True

        return False
```