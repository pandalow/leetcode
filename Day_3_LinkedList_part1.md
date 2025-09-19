[203 Remove Linked List](https://leetcode.com/problems/remove-linked-list-elements/)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        dummy_head.next = head

        prev = dummy_head
        curr = dummy_head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next

        return dummy_head.next
```
1. 用两个指针更加明确的指向 前一节点的 prev, 当前节点的 curr;
2. 使用DummyHead来处理头节点的问题;
3. 每次处理时, curr.next为空也可以指向,
4. 命中条件 val和实际前进不在一次循环中完成, 而是分开的

逻辑:
    1. 创建一个dummyHead, 它是一个虚拟head, 后面链接实际的head
        1. 相当于创建一个全新的list
    2. 获得一个前指针prev, 在dummy list上, 每次指向输入list的前一位
    3. 获得一个后指针curr, 在实际的list,每次指向输入的当前迭代位置,
    4. 用curr 遍历当前的list
        1. 如果没出现需要移除的val, 就让prev指向当前的curr(形同prev往后移动一位)
        2. 如果出现了需要移除的val, 就让prev指向curr的下一位(形同跳过当前的curr的值)
        3. 每次都是让curr 后移1位
    5. 最后返回dummyHead.next, 为真实的head



[707](https://leetcode.com/problems/design-linked-list/submissions/1776148520/)
* **始终使用 dummy 节点**，统一头插/头删逻辑，避免特判。
* **边界检查要全面**:
  * `get`：`index < 0 or index >= size → -1`
  * `addAtIndex`：`index > size → 忽略`
  * `deleteAtIndex`：`index < 0 or index >= size → 忽略`
* **插入模板**：`node.next = prev.next; prev.next = node`
* **删除模板**：`prev.next = prev.next.next`
* **尾插合法** (`index == size`)，不能被过滤掉。
* **size 必须维护正确**：插入 +1，删除 -1。
* **不要修改 self.head**，遍历用临时指针 `curr`。
* **get 越界返回 -1，不要返回 None**。

```python
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """ 
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.next.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr = self.head
        for _ in range(self.size):
            curr = curr.next
        
        curr.next = ListNode(val)
        self.size+=1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:   # 注意是 > 不是 >=
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        node = ListNode(val)
        node.next = curr.next
        curr.next = node
        self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        curr.next = curr.next.next
        self.size-=1

```



[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/submissions/1776175181/)

* prev → 反转后链表的新头
* curr → 当前正在处理的节点
* tmp → 临时保存 curr.next，避免丢链
* 最终返回 prev

1. 使用两个指针 `cur` 和 `pre` 进行迭代。`pre` 指向 `cur` 前一个节点位置。初始时，`pre` 指向 `None`，`cur` 指向 `head`。
    2. 将 `pre` 和 `cur` 的前后指针进行交换，指针更替顺序为：
        1. 使用 `next` 指针保存当前节点 `cur` 的后一个节点，即 `next = cur.next`；
        2. 断开当前节点 `cur` 的后一节点链接，将 `cur` 的 `next` 指针指向前一节点 `pre`，即 `cur.next = pre`；
        3. `pre` 向前移动一步，移动到 `cur` 位置，即 `pre = cur`；
        4. `cur` 向前移动一步，移动到之前 `next` 指针保存的位置，即 `cur = next`。
    3. 继续执行第 2 步中的 1、2、3、4。
    4. 最后等到 `cur` 遍历到链表末尾，即 `cur == None`，时，`pre` 所在位置就是反转后链表的头节点，返回新的头节点 `pre`。