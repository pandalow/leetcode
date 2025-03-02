# 707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are **0-indexed**.

Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Get the value of the `indexth` node in the linked list. If the index is invalid, return `1`.
- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Add a node of value `val` before the `indexth` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node **will not be inserted**.
- `void deleteAtIndex(int index)` Delete the `indexth` node in the linked list, if the index is valid.

**Example 1:**

```
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

```

**Constraints:**

- `0 <= index, val <= 1000`
- Please do not use the built-in LinkedList library.
- At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex` and `deleteAtIndex`.

- solution
    
    ```python
    class MyLinkedList(object):
    
        def __init__(self):
            self.head = ListNode(0)
            self.size = 0
    
        def get(self, index):
            """
            :type index: int
            :rtype: int
            """
            if index < 0 or index > self.size :
                return -1
    
            cur = self.head.next
            for i in range(index):
                cur = cur.next
            return cur.val if cur else -1
        
        def addAtIndex(self, index, val):
            """
            :type index: int
            :type val: int
            :rtype: None
            """
            if index > self.size:
                return
            if index <0:
                index = 0
      
            pre = self.head
            for _ in range(index):
                pre = pre.next
    
            node = ListNode(val)
            node.next = pre.next
            pre.next = node
            self.size += 1
    
        def addAtHead(self, val):
            """
            :type val: int
            :rtype: None
            """
            self.addAtIndex(0,val)
            
    
        def addAtTail(self, val):
            """
            :type val: int
            :rtype: None
            """
            self.addAtIndex(self.size,val)
                   
    
        def deleteAtIndex(self, index):
            """
            :type index: int
            :rtype: None
            """
            if index < 0 or index >=  self.size:
                return 
             
            pre = self.head
            for _ in range(index):
                pre = pre.next
            
            pre.next = pre.next.next
            self.size -= 1  
    
    class ListNode():
        def __init__(self,val=0,next=None):
            self.val = val
            self.next = None
    
    # Your MyLinkedList object will be instantiated and called as such:
    # obj = MyLinkedList()
    # param_1 = obj.get(index)
    # obj.addAtHead(val)
    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)
    ```
    
- explain
    
    增加self.size来规范整个list的长度
    
    - head是一个虚拟节点, 需要被跳过, 每次创建列表时, 就创建一个虚拟节点head
    - 用get方法时, 需要跳过该节点, 直接从1位开始, 获取实际的节点
    - 这也是为什么add和delete里用的pre，就是防止访问到虚拟head节点。