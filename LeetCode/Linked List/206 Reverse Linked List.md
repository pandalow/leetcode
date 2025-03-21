# 206. Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

```
Input: head = [1,2]
Output: [2,1]

```

**Example 3:**

```
Input: head = []
Output: []

```

- solution
    
    ```python
    # Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            pre = None
            cur = head
            while cur != None:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
    
    ```
    
- explain
    
    **思路 1：迭代**
    
    1. 使用两个指针 `cur` 和 `pre` 进行迭代。`pre` 指向 `cur` 前一个节点位置。初始时，`pre` 指向 `None`，`cur` 指向 `head`。
    2. 将 `pre` 和 `cur` 的前后指针进行交换，指针更替顺序为：
        1. 使用 `next` 指针保存当前节点 `cur` 的后一个节点，即 `next = cur.next`；
        2. 断开当前节点 `cur` 的后一节点链接，将 `cur` 的 `next` 指针指向前一节点 `pre`，即 `cur.next = pre`；
        3. `pre` 向前移动一步，移动到 `cur` 位置，即 `pre = cur`；
        4. `cur` 向前移动一步，移动到之前 `next` 指针保存的位置，即 `cur = next`。
    3. 继续执行第 2 步中的 1、2、3、4。
    4. 最后等到 `cur` 遍历到链表末尾，即 `cur == None`，时，`pre` 所在位置就是反转后链表的头节点，返回新的头节点 `pre`。