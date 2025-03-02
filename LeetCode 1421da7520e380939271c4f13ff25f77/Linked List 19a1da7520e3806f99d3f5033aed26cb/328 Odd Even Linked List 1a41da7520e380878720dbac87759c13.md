# 328. Odd Even Linked List

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

```

**Constraints:**

- The number of nodes in the linked list is in the range `[0, 104]`.
- `106 <= Node.val <= 106`
- My solution
    
    ```python
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution(object):
        def oddEvenList(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            odd_dummy = ListNode(0)  # 奇数链表的虚拟头
            even_dummy = ListNode(0)  # 偶数链表的虚拟头
            odd, even = odd_dummy, even_dummy
            cur, count = head, 1  # 遍历原链表
            
            while cur:
                if count % 2 == 1:
                    odd.next = cur
                    odd = odd.next
                else:
                    even.next = cur
                    even = even.next
                cur = cur.next
                count += 1  # 计数器递增
            
            even.next = None  # 避免循环引用
            odd.next = even_dummy.next  # 连接偶数链表到奇数链表后面
            return odd_dummy.next  # 返回新的链表头
    ```
    
- Reference Solution
    
    class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
    if not head or not head.next or not head.next.next:
    return head
    
    ```
        evenHead = head.next
        odd, even = head, evenHead
        isOdd = True
    
        curr = head.next.next
    
        while curr:
            if isOdd:
                odd.next = curr
                odd = curr
            else:
                even.next = curr
                even = curr
            isOdd = not isOdd
            curr = curr.next
        odd.next = evenHead
        even.next = None
        return head
    
    ```
    
- explain
    
    核心思路是建立两个linkedlist, 一个奇数, 一个偶数
    
    - 拼接两个list
    - 记住在这之前需要记录下头部