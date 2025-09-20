[24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

* 忘记 dummy.next = head
* 只写了 dummy = ListNode()，没让它指向 head，导致链表丢失。
* 返回值错误
    * 写成 return head，但交换后头结点可能改变（例如 [1,2,3,4] → [2,1,4,3]），正确的是 return dummy.next。
* 交换逻辑写错
    * 写成 curr.next = prev 或 curr.next = curr，导致链表成环。
    * 正确做法是：
        * prev = first（交换后 first 在后面）
        * curr = first.next（继续处理下一对）
* 循环条件写错
    * 有时写 while curr:，这样当只剩一个节点时还会进入循环，报错。
    * 正确条件是 while curr and curr.next: 或 while prev.next and prev.next.next:。


[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

* 思路很重要:
    * 双指针的经典应用，如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。


[160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1777075546/)

* 从某个节点开始，它们共享同一段链表（即这段链表的节点对象在内存里完全相同）。
* **节点的值 (val)**

  * 是存储在链表里的数据。
  * 两个链表可能有相同的值，但这并不代表它们在内存中是同一个节点。
  * 举个例子：

    ```
    A: 1 -> 2 -> 3
    B: 9 -> 3
    ```

    两个链表的最后一个节点的值都是 `3`，但它们在内存里是不同的对象，没有“相交”。

* **节点 (ListNode 对象)**

  * 在 Python/Java/C++ 里，一个节点是一个对象，里面存储着 `val` 和 `next`。
  * “两个链表相交”的定义是：**它们共享一段后续链表**，即从某个节点开始，两个链表的 `next` 都指向同一片内存。
  * 例子：

    ```
    A: 1 -> 2 \
                 -> 8 -> 9
    B:     4 -> 5 /
    ```

    在这里，A 和 B 从值为 8 的节点开始相交，因为这个 `8` 节点 **对象本身是同一个**。

* 思路整理:
    * 双指针对应上下双节点
    * 长链表去对齐短链表的尾部, 从而使短链表同步进行
        * 获得双方长度
        * 确保长链表 - 短链表
        * 移动长链表和短链表的同一位置
    * 长短链表同步前进, 比对节点, 从而确保相交处

[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/submissions/1777101544/)

* 快慢指针相遇 → 证明有环。
* 从头节点和相遇点同时出发，每次走一步 → 会在环入口相遇。
    * 这是因为相遇时，慢指针走了 a+b，快指针走了 a+b+k(b+c)，推出 a = k(b+c)-b，刚好等于绕环若干圈再到入口的距离。
* 返回入口节点，如果没环返回 None。

**快慢指针第一次相遇后，从 head 和相遇点同时出发，每次一步，它们一定在环入口相遇。**