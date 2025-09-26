[232](https://leetcode.com/problems/implement-queue-using-stacks/submissions/1783254833/)

1. 两个stack模拟queue的行为, 查找每次头部元素时, 需要弹出stack a, 压入 stack 2, 这样会确保该栈顺序正确.
2. empty需要查找两个栈都是空的才行.
3. 如果出现 先append, 再pop, 再append 的情况, 也是合理的, 因为始终是在检查stack2, 等到栈2 清空后才会压入新的元素


[225](https://leetcode.com/problems/implement-stack-using-queues/description/)

1. 逻辑为: 遍历队列找到最后一个元素, 单独pop出来, 类似一个滚轮的逻辑. 每次找到pop(最后元素时), 必须先滚动一下前面的元素.

```python
class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        tmp = self.queue.popleft()
        self.queue.append(tmp)

        return tmp

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue

```

[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
* 核心逻辑是对栈的应用, 必须匹配左右括号比对的情况下:
    * 左边入栈逻辑和右边的出栈的逻辑需要一致: 即第一个(, 那么倒数第一个)
    * 所以这和栈的存储逻辑是符合的
    * stack如果发现了反括号, 就查询是否现在的栈顶是不是匹配, 如果不匹配就返回错误
    * 如果没有反括号, 就是持续往里面加元素




[1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

```python
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
            
        return "".join(stack)
```

* 和括号题一样, 相对更简单一些, 只要找一样的推出栈.
* 剩下的都是unique的了