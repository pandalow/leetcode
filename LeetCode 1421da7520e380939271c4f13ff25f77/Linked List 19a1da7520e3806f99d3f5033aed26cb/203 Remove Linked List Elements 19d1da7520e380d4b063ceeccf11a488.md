# 203. Remove Linked List Elements

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

```

**Example 2:**

```
Input: head = [], val = 1
Output: []

```

**Example 3:**

```
Input: head = [7,7,7,7], val = 7
Output: []

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 104]`.
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

- solution
    
    ```python
    # Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    class Solution(object):
        def removeElements(self, head, val):
            """
            :type head: Optional[ListNode]
            :type val: int
            :rtype: Optional[ListNode]
            """
            pre = ListNode(0,head)
    
            prev, cur = pre, head
            
            while cur:
                if cur.val == val:
                    prev.next = cur.next
                else:
                    prev = cur
                
                cur = cur.next
    
            return pre.next
    ```
    
- explain
    
    双指针,
    
    1. 创建一个dummyHead, 它是一个虚拟head, 后面链接实际的head
        1. 相当于创建一个全新的list
    2. 获得一个前指针prev, 在dummy list上, 每次指向输入list的前一位
    3. 获得一个后指针curr, 在实际的list,每次指向输入的当前迭代位置,
    4. 用curr 遍历当前的list
        1. 如果没出现需要移除的val, 就让prev指向当前的curr(形同prev往后移动一位)
        2. 如果出现了需要移除的val, 就让prev指向curr的下一位(形同跳过当前的curr的值)
        3. 每次都是让curr 后移1位
    5. 最后返回dummyHead.next, 为真实的head